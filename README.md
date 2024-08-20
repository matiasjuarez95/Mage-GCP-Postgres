# Data Engineering: Mage | GCP | Postgres 

## Proyect Description
This project implements an ETL (Extract, Transform, Load) pipeline to process New York City's green taxi data for the last quarter of 2020. The pipeline is built using Mage, an open-source data pipeline tool that simplifies the process of creating, running, and managing data pipelines. Mage allows us to efficiently handle data ingestion, transformation, and export tasks in a modular and scalable way.<br>
The pipeline loads the data, performs various transformations, and writes the processed data to both a PostgreSQL database and Google Cloud Storage as Parquet files. Mage is used to orchestrate the entire ETL process, ensuring that each step is executed in the correct sequence and that the pipeline can be easily scheduled and monitored.

## Project Structure
```graphql   
├── data_loader.py        # Script for data loading
├── transformer.py        # Script for data transformation
├── data_exporter.py      # Script for exporting data to PostgreSQL and Google Cloud
├── io_config.yaml        # Configuration file for PostgreSQL connection
├── Dockerfile            # Dockerfile for containerization
├── docker-compose.yml    # Docker Compose configuration file
└── README.md             # Project description file (this file)
```
## Requirements
* Python 3.7+
* Docker and Docker Compose
* PostgreSQL
* Google Cloud Storage

# Technical Details
## Data Loading
The data loader is responsible for downloading and loading the green taxi data for October, November, and December 2020 into a Pandas DataFrame.

## Transformation
The transformations include:
* Removing rows where passenger_count and trip_distance are both 0 or null.
* Creating a new column lpep_pickup_date based on the lpep_pickup_datetime column.
* Renaming columns to snake_case.
* Three assertions to ensure data integrity:
    1. vendor_id contains only valid values.
    2. passenger_count is greater than 0.
    3. trip_distance is greater than 0.

## Data Export
The transformed data is exported to:
* PostgreSQL: Data is written to a table named green_taxi within the mage schema.
* Google Cloud Storage: Data is stored as Parquet files partitioned by lpep_pickup_date.

## Scheduling
The pipeline is scheduled to run automatically every day at 5:00 AM UTC using the built-in scheduling tool.

## Setup
1. Clone the repository to your local machine:
```bash
git clone {https://github.com/matiasjuarez95/Mage-GCP-Postgres.git}
cd Mage-GCP-Postgres
```
2. Copy the `devenv` file to `env`.
3. Create a bucket in Google Cloud Storage and set up access credentials.

## Docker
1. Build Docker image:
```bash
docker-compose build
```
2. Run the Docker container:
```bash
docker-compose up -d
```
## API to PostgreSQL
1. Update the `io_config.yaml` file with your `.env` credentials:

```yml
dev:
  # PostgreSQL
  POSTGRES_CONNECT_TIMEOUT: 10
  POSTGRES_DBNAME: "{{ env_var('POSTGRES_DBNAME') }}"
  POSTGRES_SCHEMA: "{{ env_var('POSTGRES_SCHEMA') }}" # Optional
  POSTGRES_USER: "{{ env_var('POSTGRES_USER') }}"
  POSTGRES_PASSWORD: "{{ env_var('POSTGRES_PASSWORD') }}"
  POSTGRES_HOST: "{{ env_var('POSTGRES_HOST') }}"
  POSTGRES_PORT: "{{ env_var('POSTGRES_PORT') }}"
```

## API to GCP bucket to load data.
1. Create a GCP bucket to load data.
2. Connect your service account to `mage io_config.yaml` file:
```yml
GOOGLE_SERVICE_ACC_KEY_FILEPATH: "home/src/google-cred.json"
```