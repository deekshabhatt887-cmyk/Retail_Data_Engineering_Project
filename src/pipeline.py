from extract import read_data
from transform import clean_customers, clean_products, clean_sales
from validate import validate_customers, validate_products, validate_sales
from load import load_customers, load_products, load_sales
from logger import logger

try:
    logger.info("Pipeline started")

    print("Extracting data...")
    logger.info("Extracting data")
    customers, products, sales = read_data()

    print("Transforming data...")
    logger.info("Transforming data")
    customers = clean_customers(customers)
    products = clean_products(products)
    sales = clean_sales(sales)

    print("Validating data...")
    logger.info("Validating data")
    customer_errors = validate_customers(customers)
    product_errors = validate_products(products)
    sales_errors = validate_sales(sales)

    if customer_errors or product_errors or sales_errors:
        print("Data validation failed!")
        logger.error("Data validation failed")
        logger.error(f"Customer errors: {customer_errors}")
        logger.error(f"Product errors: {product_errors}")
        logger.error(f"Sales errors: {sales_errors}")

    else:
        print("Data validation successful!")
        logger.info("Data validation successful")

        print("Loading customers...")
        logger.info("Loading customers")
        load_customers(customers)

        logger.info("Loading products")
        load_products(products)

        logger.info("Loading sales")
        load_sales(sales)

        print("Pipeline completed successfully!")
        logger.info("Pipeline completed successfully")

except Exception as error:
    logger.exception(f"Pipeline failed: {error}")
    print(f"Pipeline failed: {error}")