import urllib.request
import pandas as pd

# Global User-Agent header to bypass Wikipedia's 403 Forbidden block
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_wiki_table(url):
    """Fetches and returns the first valid pandas DataFrame found at the given Wikipedia URL."""
    req = urllib.request.Request(url, headers=HEADERS)
    
    with urllib.request.urlopen(req) as response:
        tables = pd.read_html(response.read().decode('utf-8'))
        
    for df in tables:
        # If the table has MultiIndex columns, flatten them or pick the top level
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [str(col[-1]) for col in df.columns]
        else:
            df.columns = df.columns.astype(str)
            
        df.columns = df.columns.str.strip()
        
        # Return the table if it matches either S&P 500 or NASDAQ column layouts
        if any(col in df.columns for col in ['Symbol', 'Ticker', 'Security']):
            return df
            
    raise ValueError(f"No suitable financial constituent table found at URL: {url}")

def calculate_statistics(df_sp500, nasdaq_tickers):
    """Calculates the count and percentage of S&P 500 listings that are on the NASDAQ."""
    total_sp500 = len(df_sp500)
    
    # Count how many S&P 500 symbols intersect with the NASDAQ-100 set
    nasdaq_count = df_sp500['Symbol'].isin(nasdaq_tickers).sum()
    nasdaq_percentage = (nasdaq_count / total_sp500) * 100
    
    return {
        "total_sp500": total_sp500,
        "nasdaq_count": nasdaq_count,
        "nasdaq_percentage": round(nasdaq_percentage, 2)
    }

def highlight_nasdaq(row, nasdaq_tickers):
    """Maps a row to styled HTML if the ticker is a NASDAQ constituent."""
    ticker = row['Symbol']
    if ticker in nasdaq_tickers:
        return [
            f'<span style="color: #ff4d4d; font-weight: bold;">{row["Symbol"]}</span>',
            f'<span style="color: #ff4d4d; font-weight: bold;">{row["Security"]}</span>',
            f'<span style="color: #ff4d4d; font-weight: bold;">{row["GICS Sector"]} (NASDAQ)</span>'
        ]
    else:
        return [row['Symbol'], row['Security'], f'{row["GICS Sector"]} (NYSE/Other)']

def generate_html_report(styled_df, stats, output_file):
    """Generates and writes the styled dark-mode HTML file with a top statistics summary dashboard."""
    html_output = styled_df.to_html(index=False, escape=False, classes='dataframe table')
    
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>S&P 500 Elements (NASDAQ Highlighted - Dark Mode)</title>
        <style>
            body {{ 
                font-family: 'Segoe UI', Arial, sans-serif; 
                margin: 30px; 
                background-color: #121212; 
                color: #e0e0e0; 
            }}
            h2 {{ color: #ffffff; margin-bottom: 5px; }}
            
            /* Statistics Dashboard Widgets */
            .stats-container {{
                display: flex;
                gap: 20px;
                margin: 25px 0;
            }}
            .stat-card {{
                background-color: #1e1e1e;
                padding: 20px;
                border-radius: 6px;
                min-width: 180px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                border-left: 4px solid #444;
            }}
            .stat-card.highlight {{
                border-left-color: #ff4d4d;
            }}
            .stat-label {{
                font-size: 12px;
                text-transform: uppercase;
                color: #888888;
                letter-spacing: 1px;
                margin-bottom: 5px;
            }}
            .stat-value {{
                font-size: 28px;
                font-weight: bold;
                color: #ffffff;
            }}
            .stat-value.red-text {{
                color: #ff4d4d;
            }}

            table {{ 
                border-collapse: collapse; 
                width: 100%; 
                background-color: #1e1e1e; 
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3); 
                margin-top: 20px;
            }}
            th {{ 
                background-color: #2a2a2a; 
                color: #ffffff; 
                font-weight: 600;
                padding: 14px 12px;
                text-align: left;
                border-bottom: 2px solid #333333;
            }}
            td {{ 
                padding: 12px; 
                text-align: left; 
                border-bottom: 1px solid #2d2d2d;
                color: #cccccc;
            }}
            tr:nth-child(even) {{ background-color: #161616; }}
            tr:hover {{ background-color: #262626; }}
        </style>
    </head>
    <body>
        <h2>S&P 500 Index Constituents</h2>
        
        <div class="stats-container">
            <div class="stat-card">
                <div class="stat-label">Total S&P 500 Listings</div>
                <div class="stat-value">{stats['total_sp500']}</div>
            </div>
            <div class="stat-card highlight">
                <div class="stat-label">NASDAQ-100 Listings</div>
                <div class="stat-value red-text">{stats['nasdaq_count']}</div>
            </div>
            <div class="stat-card highlight">
                <div class="stat-label">Index Representation</div>
                <div class="stat-value red-text">{stats['nasdaq_percentage']}%</div>
            </div>
        </div>

        {html_output}
    </body>
    </html>
    """
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_template)

def main():
    """Main execution orchestrator."""
    sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    nasdaq_url = "https://en.wikipedia.org/wiki/NASDAQ-100"
    output_filename = "sp500_highlighted_dark.html"
    
    # 1. Fetch data
    print("Fetching live S&P 500 constituents...")
    df_sp500_raw = fetch_wiki_table(sp500_url)
    df_sp500 = df_sp500_raw[['Symbol', 'Security', 'GICS Sector']].copy()
    
    print("Fetching NASDAQ-100 constituents...")
    df_nasdaq = fetch_wiki_table(nasdaq_url)
    nasdaq_column = 'Ticker' if 'Ticker' in df_nasdaq.columns else 'Symbol'
    nasdaq_tickers = set(df_nasdaq[nasdaq_column].tolist())
    
    # 2. Run statistical calculations
    stats = calculate_statistics(df_sp500, nasdaq_tickers)
    
    # 3. Process and style the components
    print("Processing and styling all 500+ constituents...")
    styled_rows = []
    for _, row in df_sp500.iterrows():
        styled_rows.append(highlight_nasdaq(row, nasdaq_tickers))
        
    styled_df = pd.DataFrame(styled_rows, columns=['Ticker', 'Company Name', 'Sector / Exchange'])
    
    # 4. Output dark-mode report with integrated stats block
    generate_html_report(styled_df, stats, output_filename)
    print(f"Success! Full dark-mode table with statistics preview saved to: '{output_filename}'")

if __name__ == "__main__":
    main()