# Retail Data Engineering Project

## 📌 Project Overview

This project is an end-to-end retail data engineering pipeline that extracts raw sales data from object storage, transforms and validates the data using Python, loads it into PostgreSQL, and provides an interactive Streamlit dashboard for business analytics.

The project also uses Docker to create a reproducible environment and MinIO as an S3-compatible object storage system for raw data.

## 🏗️ Architecture

```text
                 Raw CSV Data
                      │
                      ▼
               ┌─────────────┐
               │    MinIO    │
               │ S3-compatible│
               │   Storage   │
               └──────┬──────┘
                      │
                      ▼
              ┌──────────────┐
              │ Python ETL   │
              │              │
              │ Extract      │
              │ Transform    │
              │ Validate     │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │  PostgreSQL  │
              │   Database   │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │  Streamlit   │
              │  Dashboard   │
              └──────────────┘

                 Docker
        ─────────────────────
        Provides reproducible
        application environments
```

## 🛠️ Technologies Used

* Python
* Pandas
* MinIO
* PostgreSQL
* SQLAlchemy
* Psycopg
* Streamlit
* Docker
* Docker Compose
* Pytest
* Git & GitHub

## 🔄 ETL Process

### 1. Extract

The pipeline reads:

* `customers.csv`
* `products.csv`
* `sales.csv`

from the MinIO `retail-data` bucket.

### 2. Transform

Python and Pandas are used to clean and prepare the data, including handling duplicates, missing values, data types, and other data-quality requirements.

### 3. Validate

The pipeline checks customer, product, and sales data before loading.

If validation fails, the loading process is stopped.

### 4. Load

Validated data is loaded into PostgreSQL tables:

* `customers`
* `products`
* `sales`

The loading process uses conflict handling to avoid duplicate primary-key failures when the pipeline is executed repeatedly.

### 5. Analytics

SQL-based analytics are used to generate:

* Total sales
* Monthly sales
* Top-selling products
* Sales by city
* Sales by category
* Top customers
* Dashboard summary metrics

### 6. Dashboard

Streamlit provides an interactive dashboard with date filtering and visualizations for sales and customer analysis.

## 📁 Project Structure

```text
Retail_Data_Engineering_Project/
│
├── data/
│   └── raw/
│
├── minio-data/
│
├── logs/
│
├── src/
│   ├── analytics.py
│   ├── dashboard.py
│   ├── database.py
│   ├── extract.py
│   ├── load.py
│   ├── logger.py
│   ├── pipeline.py
│   ├── transform.py
│   └── validate.py
│
├── tests/
│   ├── test_pipeline.py
│   ├── test_transform_run.py
│   └── test_validate_run.py
│
├── .dockerignore
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/deekshabhatt887-cmyk/Retail_Data_Engineering_Project.git
cd Retail_Data_Engineering_Project
```

### 2. Create and activate the virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file with your PostgreSQL connection details.

Do not commit `.env` to GitHub.

### 5. Start MinIO and the dashboard

```powershell
docker compose up -d --build
```

### 6. Run the ETL pipeline

```powershell
python src/pipeline.py
```

### 7. Open the dashboard

```text
http://localhost:8501
```

### 8. Open MinIO Console

```text
http://localhost:9001
```

## 🧪 Testing

Run all tests with:

```powershell
pytest
```

The project uses automated tests to verify data transformation, validation, and pipeline-related functionality.

## 📊 Dashboard Features

The dashboard provides:

* Total Sales
* Units Sold
* Customer Count
* Products Sold
* Monthly Sales Trends
* Top-Selling Products
* Sales by City
* Sales by Category
* Top Customers
* Date-range filtering

## 🔐 Security

Database credentials are stored in environment variables using `.env`.

The `.env` file is excluded from Git using `.gitignore`.

## 🎯 Key Data Engineering Concepts Demonstrated

This project demonstrates practical understanding of:

* ETL pipelines
* Object storage
* S3-compatible storage
* Data cleaning
* Data validation
* PostgreSQL
* SQL analytics
* Database connectivity
* Logging
* Automated testing
* Docker
* Docker Compose
* Environment variables
* Dashboard development
* Git and GitHub

## Author

Deeksha Bhatt
