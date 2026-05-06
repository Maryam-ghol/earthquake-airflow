import json
from datetime import datetime
from pathlib import Path
import pandas as pd

from scripts.utils.logger import logger

PROCESSED_DATA_PATH = Path("data/processed")
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

# Accept Airflow runtime metadata.--> **context
def normalize_earthquake_data(input_file=None, **context):

    # 📌 If running inside Airflow → use XCom----“Get data returned from the fetch_earthquake_data task.”
    # context['ti']-> task instance object → xcom_pull() to get data from another task
    if input_file is None:
        input_file = context['ti'].xcom_pull(
            task_ids='clean_earthquake_data'
        )

    logger.info(f"Reading earthquake data from: {input_file}")

    with open(input_file, "r") as f:
        data = json.load(f)

    # ✅ Keep only earthquakes with valid magnitude
    normalized_data = []

    for earthquake in data:
        props = earthquake["properties"]
        coords = earthquake["geometry"]["coordinates"]

        normalized_data.append({
            "mag": props.get("mag"),
            "place": props.get("place"),
            "time": props.get("time"),
            "latitude": coords[1],
            "longitude": coords[0],
            "depth": coords[2]
        })
   

    filename = f"normalized_earthquakes_{datetime.now().date()}.csv"

    file_path = PROCESSED_DATA_PATH / filename

    df = pd.DataFrame(normalized_data)
    df.to_csv(file_path, index=False)

    logger.info(f"Saved normalized data to: {file_path}")

    return str(file_path)


if __name__ == "__main__":

    latest_file = sorted(PROCESSED_DATA_PATH.glob("*.json"))[-1]
    logger.info(f"Reading earthquake data from: {latest_file}")

    normalize_earthquake_data(input_file=str(latest_file))