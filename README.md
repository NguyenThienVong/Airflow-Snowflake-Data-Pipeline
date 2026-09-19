# ✈️ Flight Operations Data Pipeline

A beginner-friendly Data Engineering project that collects flight data from the OpenSky API, processes it using Python and Apache Airflow, and stores analytical data in Snowflake.

## 🏗️ Data Architecture

![Flight Operations Architecture](docs/flight-operations-architecture.png)

🔗 [View Architecture Diagram on Lucidchart](https://lucid.app/lucidchart/4d0c0f98-b78c-49b6-8961-814832cd4d83/edit?viewport_loc=-59%2C24%2C1599%2C872%2C0_0&invitationId=inv_e3ff2ea8-60be-4278-ba0f-a3f51260fb87)
<img width="1580" height="790" alt="Screenshot 2026-09-19 191041" src="https://github.com/user-attachments/assets/a82cd1e2-71fc-4d9b-83c7-68ea7d9aa49d" />

## 🔄 Pipeline Workflow

```text
OpenSky API
    ↓
Bronze: Raw Data
    ↓
Silver: Cleaned Data
    ↓
Gold: Aggregated Data
    ↓
Snowflake
    ↓
Streamlit Dashboard
```

Apache Airflow is used to schedule and manage the pipeline.

## 🛠️ Technologies

- Python
- Pandas
- Apache Airflow
- Docker
- Snowflake
- Streamlit
- Git & GitHub

## 📌 What I Learned

- Extracting data from an API
- Cleaning and transforming data with Pandas
- Building an ETL pipeline
- Using Apache Airflow to schedule tasks
- Loading data into Snowflake
- Creating a simple data dashboard

## 🚀 Future Improvements

- Add data quality checks
- Improve error handling
- Add more dashboard features
- Learn and implement dbt

## 👨‍💻 Author

Nguyen Thien Vong

Aspiring Data Engineer
