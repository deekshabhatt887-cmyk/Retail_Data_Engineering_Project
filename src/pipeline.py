from extract import read_data
from transform import clean_customers, clean_products, clean_sales
from validate import validate_customers, validate_products, validate_sales
from load import load_customers, load_products, load_sales

print("Extracting data...")

customers, products, sales = read_data()

print("Transforming data...")

customers = clean_customers(customers)
products = clean_products(products)
sales = clean_sales(sales)

print("Validating data...")

customer_errors = validate_customers(customers)
product_errors = validate_products(products)
sales_errors = validate_sales(sales)

if customer_errors or product_errors or sales_errors:

    print("Data validation failed!")

    print(customer_errors)
    print(product_errors)
    print(sales_errors)

else:

    print("Data validation successful!")

    print("Loading customers...")
    load_customers(customers)

    print("Loading products...")
    load_products(products)

    print("Loading sales...")
    load_sales(sales)

    print("Pipeline completed successfully!")