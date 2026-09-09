# Retail Data Engineering Project

An end-to-end retail data engineering project built using Python, PostgreSQL, SQLAlchemy, Pandas, and Streamlit.

The project demonstrates a complete data pipeline:

**Extract → Transform → Validate → Load → Analyze → Visualize**

---

## Project Overview

This project processes retail data containing:

- Customers
- Products
- Sales

The pipeline reads raw CSV files, cleans and validates the data, loads it into PostgreSQL, performs SQL-based analytics, and displays the results through an interactive Streamlit dashboard.

---

## Technologies Used

- Python
- Pandas
- PostgreSQL
- Psycopg
- SQLAlchemy
- Streamlit
- Git
- GitHub

---

## Project Architecture

```text
Retail_Data_Engineering_Project/
│
├── config/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│
├── logs/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── database.py
│   ├── analytics.py
│   ├── pipeline.py
│   ├── logger.py
│   └── dashboard.py
│
├── tests/
│
├── ui/
│
├── .gitignore
├── requirements.txt
└── README.md

Data Pipeline
1. Extract

Raw CSV files are read from the data/raw directory using Pandas.

Input datasets include:

customers.csv
products.csv
sales.csv
2. Transform

The raw data is cleaned and transformed before loading.

Examples include:

Handling missing values
Cleaning data types
Preparing data for database loading
3. Validate

The pipeline validates the datasets before loading them into PostgreSQL.

If validation fails, the pipeline stops and displays the validation errors.

4. Load

Validated data is loaded into PostgreSQL.

The project uses:

Psycopg for PostgreSQL connectivity
SQLAlchemy for database interaction
5. Analyze

SQL queries are used to generate business insights such as:

Total sales
Monthly sales
Top-selling products
Sales by city
Sales by category
Top customers
6. Visualize

The analytics results are displayed using an interactive Streamlit dashboard.

The dashboard includes:

KPI cards
Sales charts
Product analysis
Customer analysis
Category analysis
City-wise sales
Date range filtering
Database

The PostgreSQL database contains the following main tables:

Customers

Stores customer information.

customer_id
customer_name
email
city
state
Products

Stores product information.

product_id
product_name
category
price
stock_quantity
Sales

Stores sales transactions.

order_id
customer_id
product_id
quantity
order_date
store
How to Run the Project
1. Clone the repository
git clone https://github.com/deekshabhatt887-cmyk/Retail_Data_Engineering_Project.git
2. Navigate to the project
cd Retail_Data_Engineering_Project
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
6. Configure environment variables

Create a .env file in the project root:

DB_HOST=localhost
DB_NAME=retail_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432

Do not commit the .env file to GitHub.

7. Run the pipeline
python src/pipeline.py

The pipeline will:

Extract
   ↓
Transform
   ↓
Validate
   ↓
Load
8. Run the Streamlit dashboard
streamlit run src/dashboard.py

The dashboard will open in your browser.

Example Analytics

The project can answer questions such as:

What are the total sales?
Which products sell the most?
Which cities generate the highest sales?
Which categories generate the most revenue?
Who are the top customers?
How do sales change over time?
Data Engineering Concepts Demonstrated

This project demonstrates practical knowledge of:

ETL pipelines
Data extraction
Data transformation
Data validation
PostgreSQL
SQL queries
Database connectivity
SQLAlchemy
Pandas
Data quality checks
Logging
Environment variables
Error handling
Data analytics
Streamlit dashboards
Git and GitHub
Future Improvements

Possible future enhancements include:

AWS cloud deployment
Apache Airflow orchestration
Docker containerization
Automated testing with CI/CD
Cloud data warehouse integration
Incremental data loading
Advanced data quality monitoring
Data pipeline scheduling
Author

Deeksha Bhatt

This project was created as part of a practical Data Engineering learning journey.