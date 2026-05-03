import json
from datetime import datetime
from pathlib import Path

from scripts.utils.logger import logger


RAW_DATA_PATH = Path("data/raw")
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

PROCESSED_DATA_PATH = Path("data/processed")
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)


def clean_earthquake_data(input_file=None, **context):

    # 📌 If running inside Airflow → use XCom----“Get data returned from the fetch_earthquake_data task.”
    if input_file is None:
        input_file = context['ti'].xcom_pull(
            task_ids='fetch_earthquake_data'
        )

    logger.info(f"Reading earthquake data from: {input_file}")

    with open(input_file, "r") as f:
        data = json.load(f)

    # ✅ Keep only earthquakes with valid magnitude
    cleaned_data = [
        earthquake
        for earthquake in data['features']
        if earthquake['properties']['mag'] is not None
    ]

    filename = f"cleaned_earthquakes_{datetime.now().date()}.json"

    file_path = PROCESSED_DATA_PATH / filename

    with open(file_path, "w") as f:
        json.dump(cleaned_data, f, indent=4)

    logger.info(f"Saved cleaned data to: {file_path}")

    return str(file_path)


if __name__ == "__main__":

    latest_file = sorted(RAW_DATA_PATH.glob("*.json"))[-1]

    clean_earthquake_data(input_file=str(latest_file))