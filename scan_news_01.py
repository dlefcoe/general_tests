import collections
import os
import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.newsnow.co.uk/h/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


def get_top_headlines(url):
    print(f"Fetching headlines from {url}...")
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    all_links = soup.find_all("a")

    for el in all_links:
        text = el.get_text(strip=True)
        if text and len(text) > 25:
            if any(
                skip in text.lower()
                for skip in [
                    "terms of use",
                    "privacy policy",
                    "cookie policy",
                    "manage cookies",
                    "all rights reserved",
                ]
            ):
                continue
            headlines.append(text)

    return list(set(headlines))


def generate_html_dashboard(headlines, top_n=20):
    if not headlines:
        print("No headlines found to generate dashboard.")
        return

    # Process words
    all_text = " ".join(headlines).lower()
    words = re.findall(r"\b\w+\b", all_text)

    stop_words = {
        "the",
        "to",
        "and",
        "a",
        "in",
        "of",
        "for",
        "on",
        "is",
        "at",
        "with",
        "by",
        "as",
        "from",
        "it",
        "that",
        "this",
        "after",
        "over",
        "new",
        "says",
        "will",
        "are",
        "be",
        "us",
        "uk",
        "i",
        "you",
        "he",
        "she",
        "has",
        "have",
        "was",
        "about",
        "more",
        "news",
        "view",
        "headlines",
        "latest",
        "hours",
        "ago",
        "minutes",
    }
    filtered_words = [
        word for word in words if word not in stop_words and len(word) > 2
    ]

    word_counts = collections.Counter(filtered_words)
    most_common = word_counts.most_common(top_n)

    # Calculate percentages for simple data bar visual
    max_count = most_common[0][1] if most_common else 1

    # Generate HTML Table rows for Data
    table_rows = ""
    for rank, (word, count) in enumerate(most_common, 1):
        percentage = (count / max_count) * 100
        table_rows += f"""
        <tr>
            <td>{rank}</td>
            <td style="font-weight: bold; color: #1e293b;">{word}</td>
            <td><span class="badge">{count}</span></td>
            <td>
                <div class="bar-container">
                    <div class="bar" style="width: {percentage}%;"></div>
                </div>
            </td>
        </tr>
        """

    # Generate HTML Headlines List items
    headlines_li = "".join(
        [
            f"<li>{html_escape(headline)}</li>"
            for headline in sorted(headlines)[:100]
        ]
    )

    # HTML Template
    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NewsNow Trend Analysis</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #f8fafc;
                color: #334155;
                margin: 0;
                padding: 40px 20px;
            }}
            .container {{
                max-width: 1100px;
                margin: 0 auto;
            }}
            header {{
                margin-bottom: 30px;
                border-bottom: 2px solid #e2e8f0;
                padding-bottom: 20px;
            }}
            h1 {{ color: #0f172a; margin: 0 0 10px 0; font-size: 28px; }}
            .meta {{ color: #64748b; font-size: 14px; }}
            
            .grid {{
                display: grid;
                grid-template-columns: 1.2fr 1fr;
                gap: 30px;
            }}
            @media (max-width: 850px) {{
                .grid {{ grid-template-columns: 1fr; }}
            }}
            
            .card {{
                background: white;
                border-radius: 8px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                padding: 24px;
                border: 1px solid #e2e8f0;
            }}
            h2 {{ color: #1e293b; font-size: 18px; margin-top: 0; margin-bottom: 20px; }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                text-align: left;
            }}
            th, td {{
                padding: 12px;
                border-bottom: 1px solid #f1f5f9;
                font-size: 14px;
            }}
            th {{ color: #64748b; font-weight: 600; }}
            
            .badge {{
                background-color: #e0f2fe;
                color: #0369a1;
                padding: 4px 8px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12px;
            }}
            .bar-container {{
                background: #f1f5f9;
                border-radius: 4px;
                height: 12px;
                width: 100%;
                overflow: hidden;
            }}
            .bar {{
                background: #3b82f6;
                height: 100%;
                border-radius: 4px;
            }}
            
            .headline-list {{
                max-height: 600px;
                overflow-y: auto;
                padding-right: 10px;
            }}
            ul {{ padding-left: 20px; margin: 0; }}
            li {{ margin-bottom: 10px; font-size: 13.5px; line-height: 1.5; color: #475569; }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>NewsNow Dynamic Keyword Tracker</h1>
                <div class="meta">Analyzed <strong>{len(headlines)} unique headlines</strong> directly from the main feed.</div>
            </header>
            
            <div class="grid">
                <div class="card">
                    <h2>Frequency Breakdown (Top {top_n} Words)</h2>
                    <table>
                        <thead>
                            <tr>
                                <th style="width: 8%;">Rank</th>
                                <th style="width: 30%;">Keyword</th>
                                <th style="width: 15%;">Mentions</th>
                                <th style="width: 47%;">Density Distribution</th>
                            </tr>
                        </thead>
                        <tbody>
                            {table_rows}
                        </tbody>
                    </table>
                </div>
                
                <div class="card">
                    <h2>Scraped Headlines Repository (Sample Feed)</h2>
                    <div class="headline-list">
                        <ul>
                            {headlines_li}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    output_filename = "news_analysis.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"\n[+] Success! Analysis dashboard saved to: {os.path.abspath(output_filename)}")
    print("Double-click that file to open your visual layout directly in any browser.")


def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


if __name__ == "__main__":
    headlines = get_top_headlines(URL)
    if headlines:
        generate_html_dashboard(headlines)
    else:
        print("Scraper returned zero items. Verify connections.")


        