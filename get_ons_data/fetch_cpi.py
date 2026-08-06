import io

import pandas as pd
import requests

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch_ons_timeseries(
    cdid: str, dataset_id: str, topic_path: str
) -> pd.DataFrame:
    """Fetch ONS timeseries data by CDID and path components."""
    base_url = "https://www.ons.gov.uk/generator"
    uri = f"/{topic_path.strip('/')}/timeseries/{cdid.lower()}/{dataset_id.lower()}"

    params = {"format": "csv", "uri": uri}

    res = requests.get(base_url, headers=HEADERS, params=params)
    res.raise_for_status()

    # Skip 8 metadata rows to parse the data table
    return pd.read_csv(
        io.StringIO(res.text), skiprows=8, names=["Date", "Value"]
    )


# Example usage:
# Fetch CPI Index (CDID: L522)
df_cpi = fetch_ons_timeseries(
    cdid="l522",
    dataset_id="mm23",
    topic_path="economy/inflationandpriceindices",
)

print(df_cpi.head())