import json
from datetime import datetime, timedelta
from pathlib import Path
from scripts.utils.logger import logger


RAW_DATA_PATH = Path("data/raw")
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

PROCESSED_DATA_PATH = Path("data/processed")
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

def clean_earthquake_data(**context):
    logger.info(f"Reading earthquakes dat from json file: {context['ti'].xcom_pull(task_ids='fetch_earthquake_data')}")

    with open(context['ti'].xcom_pull(task_ids='fetch_earthquake_data'), "r") as f:
        data = json.load(f)

    # Perform cleaning operations on the data
    cleaned_data = [earthquake for earthquake in data['features'] if earthquake['properties']['mag'] is not None]

    # Save the cleaned data
    filename = f"cleaned_earthquakes_{datetime.now().date()}.json"
    file_path = PROCESSED_DATA_PATH / filename

    with open(file_path, "w") as f:
        json.dump(cleaned_data, f, indent=4)

    logger.info(f"Saved cleaned data to: {file_path}")

    return str(file_path)

    
if __name__ == "__main__":
    clean_earthquake_data()