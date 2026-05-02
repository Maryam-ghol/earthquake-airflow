🌍 Earthquake Data Pipeline with Apache Airflow
## 📌 Overview

This project is an end-to-end ETL data pipeline built with Apache Airflow that automatically collects, processes, and analyzes global earthquake data from the USGS API.

The pipeline is designed to simulate a real-world data engineering workflow, including ingestion, transformation, storage, and reporting.

## 🎯 Objectives
Automate earthquake data ingestion from a public API
Clean and transform raw JSON data into structured format
Store processed data for analytics
Detect significant seismic events
Generate daily reports
Practice real-world Airflow orchestration patterns
## 🏗️ Architecture
USGS Earthquake API
        ↓
Apache Airflow DAG
        ↓
Fetch Raw Data (JSON)
        ↓
Data Cleaning & Transformation (Pandas)
        ↓
PostgreSQL Storage
        ↓
Analytics & Aggregation
        ↓
Report Generation (CSV)
## ⚙️ Tech Stack
Apache Airflow – Workflow orchestration
Python – Data processing
Pandas – Data transformation
PostgreSQL – Data storage
Docker – Containerized environment
USGS API – Earthquake data source
## 📂 Project Structure

```text
earthquake-airflow/
│
├── dags/
│   └── earthquake_pipeline_dag.py
│
├── scripts/
│   ├── fetch/
│   ├── processing/
│   ├── database/
│   ├── analytics/
│   └── reporting/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── sql/
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Workflow

1. **Fetch Data**
   - Extract earthquake data from the USGS API
   - Store raw JSON files in `data/raw/`

2. **Data Cleaning**
   - Parse and normalize JSON structure
   - Extract relevant fields (time, magnitude, location)
   - Handle missing or inconsistent values

3. **Data Storage**
   - Load cleaned data into PostgreSQL database
   - Ensure structured and queryable format

4. **Analytics**
   - Compute daily statistics (count, mean magnitude, max magnitude)
   - Identify significant earthquake events

5. **Reporting**
   - Generate daily summary reports
   - Export results as CSV files in `data/processed/`
🚀 How to Run
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/earthquake-airflow.git
cd earthquake-airflow
2. Start Airflow with Docker
docker-compose up
3. Open Airflow UI

Visit:

http://localhost:8080

Login:

Username: airflow
Password: airflow
📊 Example Output
Daily earthquake dataset
Cleaned structured tables in PostgreSQL
CSV reports with:
Earthquake counts per day
Average magnitude
Strong earthquake detection (M ≥ 5.0)
📌 Key Features
Fully automated ETL pipeline
Modular and scalable architecture
Dockerized setup for easy deployment
Airflow best practices (task separation, retries, scheduling)
Real-world public dataset integration
🧠 What I Learned
Designing Airflow DAGs for ETL workflows
Structuring production-like data pipelines
Working with external APIs in scheduled jobs
Data cleaning and transformation with Pandas
Containerized workflow orchestration using Docker

📄 License

This project is open-source and available under the MIT License.

👤 Author

Built by Maryam Gholamicherovi
Data Engineer 
Focused on data pipelines