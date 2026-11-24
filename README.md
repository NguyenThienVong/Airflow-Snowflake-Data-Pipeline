✈️ Flight Operations Data Pipeline

An end-to-end Data Engineering project that extracts flight tracking data from the OpenSky Network API, processes it through a Medallion Architecture (Bronze, Silver, Gold), and loads analytical data into Snowflake.

The pipeline is orchestrated using Apache Airflow and containerized with Docker, with a Streamlit dashboard for data visualization.

This project demonstrates practical skills in API data ingestion, ETL development, data transformation, workflow orchestration, cloud data warehousing, and data visualization.

---

📌 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Technologies Used](#-technologies-used)
- [Data Architecture](#-data-architecture)
- [Pipeline Workflow](#-pipeline-workflow)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation and Setup](#-installation-and-setup)
- [Running the Pipeline](#-running-the-pipeline)
- [Data Storage Architecture](#-data-storage-architecture)
- [Dashboard](#-dashboard)
- [Lessons Learned](#-lessons-learned)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

🎯 Project Overview

The Flight Operations Data Pipeline is designed to automate the collection and processing of flight tracking data from the OpenSky Network API.

The project follows a Medallion Architecture to organize data into three layers:

- Bronze Layer: Stores raw data extracted from the API.
- Silver Layer: Contains cleaned and transformed data.
- Gold Layer: Stores aggregated data prepared for analytical purposes.

Apache Airflow manages the workflow and schedules pipeline execution, while Snowflake serves as the analytical data warehouse.

Project Objectives

- Build an automated ETL pipeline using Python.
- Extract real-world flight data from a REST API.
- Implement Bronze, Silver, and Gold data layers.
- Orchestrate ETL workflows using Apache Airflow.
- Load processed data into Snowflake.
- Containerize the development environment using Docker.
- Visualize analytical results through Streamlit.

---

💼 Business Problem

Flight tracking data can provide valuable insights into flight operations, geographical distribution, and aviation activity.

However, raw API data is not immediately suitable for analytical purposes.

This project addresses the following challenges:

1. Data Ingestion: Retrieve flight data from an external API.
2. Data Processing: Clean and transform raw records into structured datasets.
3. Data Organization: Separate raw, cleaned, and aggregated data using a Medallion Architecture.
4. Workflow Automation: Schedule and orchestrate data processing tasks.
5. Analytics: Store processed data in Snowflake for downstream analysis.

The final objective is to create a repeatable data pipeline that transforms raw flight tracking data into analytical datasets.

---

🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | ETL development |
| Pandas | Data cleaning and transformation |
| Requests | API data extraction |
| OpenSky Network API | Flight tracking data source |
| Apache Airflow 2.9.3 | Workflow orchestration |
| Docker Compose | Container management |
| PostgreSQL 15 | Airflow metadata database |
| Snowflake | Cloud data warehouse |
| Streamlit | Data visualization |
| Git & GitHub | Version control |

---

🏗️ Data Architecture

The project follows a Medallion Architecture consisting of Bronze, Silver, and Gold layers.

Architecture Diagram:

[View Architecture Diagram on Lucidchart](https://lucid.app/lucidchart/4d0c0f98-b78c-49b6-8961-814832cd4d83/edit?viewport_loc=-59%2C24%2C1599%2C872%2C0_0&invitationId=inv_e3ff2ea8-60be-4278-ba0f-a3f51260fb87)
<img width="1580" height="790" alt="Screenshot 2026-09-19 191041" src="https://github.com/user-attachments/assets/a82cd1e2-71fc-4d9b-83c7-68ea7d9aa49d" />

Architecture Components

| Component | Responsibility |
|---|---|
| OpenSky API | Provides flight tracking data |
| Python | Extracts and processes data |
| Bronze Layer | Stores raw API data |
| Silver Layer | Stores cleaned and transformed data |
| Gold Layer | Stores aggregated analytical data |
| Apache Airflow | Orchestrates pipeline execution |
| Snowflake | Stores analytical data |
| Streamlit | Presents analytical results |

---

🔄 Pipeline Workflow

The pipeline follows these stages:

1. Extract – API Ingestion

- Connect to the OpenSky Network API.
- Retrieve flight tracking information.
- Extract raw API responses for downstream processing.

2. Bronze – Raw Data

- Store the extracted raw data.
- Preserve the original data before transformation.

3. Silver – Data Cleaning

- Process raw data using Pandas.
- Clean and transform records.
- Prepare structured datasets for analytical processing.

4. Gold – Data Aggregation

- Aggregate processed flight data.
- Prepare datasets for analytical queries and visualization.

5. Load – Snowflake

- Connect to Snowflake.
- Load processed analytical data into the data warehouse.

6. Visualization – Streamlit

- Connect to the processed analytical data.
- Present flight operation insights through a dashboard.

Apache Airflow orchestrates and schedules the workflow.

---

📁 Project Structure

```text
Airflow-Snowflake-Data-Pipeline/
│
├── dags/
│   └── flights_ops_medallion_pipe.py
│
├── scripts/
│   └── ETL processing scripts
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── png/
│   └── Project screenshots and diagrams
│
├── docker-compose.yaml
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

Note: Update the file names above to match the actual files in the repository.

---

⚙️ Prerequisites

Before running this project, make sure you have installed:

- Python 3.x
- Docker Desktop
- Docker Compose
- A Snowflake account
- Git

You will also need access to the OpenSky Network API.

---

🚀 Installation and Setup

Step 1: Clone the Repository

```bash
git clone https://github.com/NguyenThienVong/Airflow-Snowflake-Data-Pipeline.git

cd Airflow-Snowflake-Data-Pipeline
```

Step 2: Configure Environment Variables

Create a local `.env` file based on `.env.example`.

Example:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=flightsdb

AIRFLOW_ADMIN_USER=admin
AIRFLOW_ADMIN_FIRSTNAME=Admin
AIRFLOW_ADMIN_LASTNAME=User
AIRFLOW_ADMIN_EMAIL=admin@example.com
AIRFLOW_ADMIN_PASSWORD=your_password
```

Important: Never commit `.env` or any credentials to GitHub.

Step 3: Configure Snowflake Connection

Configure the Snowflake connection in the Apache Airflow interface.

Use the following connection ID:

```text
flight_snowflake
```

Add the required Snowflake connection credentials and configuration according to your Snowflake account.

Step 4: Initialize Airflow

Run the following command:

```bash
docker compose up airflow-init
```

This initializes the Airflow metadata database and creates the Airflow administrator account.

Step 5: Start the Services

```bash
docker compose up -d
```

Check running containers:

```bash
docker compose ps
```

---

▶️ Running the Pipeline

Once the Docker services are running:

1. Open the Airflow web interface:

   ```text
   http://localhost:8080
   ```

2. Log in using the administrator credentials configured in `.env`.

3. Locate the DAG:

   ```text
   flights_ops_medallion_pipe
   ```

4. Enable the DAG if it is paused.

5. Trigger the DAG manually or allow the scheduler to execute it automatically.

6. Monitor task execution and logs through the Airflow interface.

To view scheduler logs:

```bash
docker compose logs -f airflow-scheduler
```

To stop the services:

```bash
docker compose down
```

---

🗄️ Data Storage Architecture

The project uses a Medallion Architecture to organize data throughout the pipeline.

| Layer | Description | Purpose |
|---|---|---|
| Bronze | Raw flight data | Preserve source data |
| Silver | Cleaned flight data | Improve data consistency |
| Gold | Aggregated flight data | Support analytical queries |

Snowflake is used as the analytical data warehouse for processed data.

---

📊 Dashboard

Streamlit is used to visualize processed flight operation data.

The dashboard provides a visual interface for exploring analytical results generated by the pipeline.

Dashboard Preview:

<!-- Add your actual dashboard screenshot here -->

```text
Replace this section with your dashboard screenshot.
```

---

📚 Lessons Learned

Through this project, I gained practical experience in:

- Extracting data from REST APIs using Python.
- Processing and transforming datasets with Pandas.
- Understanding and implementing Medallion Architecture.
- Building ETL workflows with modular Python scripts.
- Orchestrating data pipelines using Apache Airflow.
- Working with Docker Compose and containerized environments.
- Connecting Python applications to Snowflake.
- Understanding the role of cloud data warehouses in analytical workflows.
- Building data visualization applications with Streamlit.

---

🔮 Future Improvements

Potential improvements for future development:

- Implement automated data quality checks.
- Improve error handling and logging mechanisms.
- Introduce incremental data loading.
- Integrate dbt for data transformation and modeling.
- Add pipeline monitoring and alerting.
- Improve dashboard functionality.
- Implement automated testing for ETL components.

---

👨‍💻 Author

Nguyen Thien Vong

Aspiring Data Engineer

- GitHub: [NguyenThienVong](https://github.com/NguyenThienVong)

---

⭐ If you find this project interesting, feel free to explore the repository!
