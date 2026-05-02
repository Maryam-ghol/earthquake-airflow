import requests
import json
from datetime import datetime, timedelta
from pathlib import Path


USGS_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"


RAW_DATA_PATH = Path("data/raw")
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)


def fetch_earthquake_data(**context):
    """
    Fetch earthquake data from USGS API for the last 1 day
    and save it as a raw JSON file.
    """

    # 📅 Define time window (last 1 day)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    params = {
        "format": "geojson",
        "starttime": start_time.strftime("%Y-%m-%d"),
        "endtime": end_time.strftime("%Y-%m-%d"),
        "minmagnitude": 0
    }

    print(f"Fetching earthquakes from {params['starttime']} to {params['endtime']}")

    response = requests.get(USGS_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")

    data = response.json()

    # 🗂 Save file with timestamp
    filename = f"earthquakes_{start_time.date()}_{end_time.date()}.json"
    file_path = RAW_DATA_PATH / filename

    with open(file_path, "w") as f:
        json.dump(data, f)

    print(f"Saved raw data to: {file_path}")

    
    
    return str(file_path)