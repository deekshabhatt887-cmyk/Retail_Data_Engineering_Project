from extract import read_data
from transform import(
    clean_customers,
    clean_products,
    clean_sales
)

from validate import(
    validate_customers,
    validate_products,
    validate_sales
)

#extract data
customers, products, sales = read_data() 

#transform data

customers = clean_customers(customers)

products = clean_products(products)

sales = clean_sales(sales)

#validate customers
customer_errors = validate_customers(customers)
print("CUSTOMER VALIDATION")

if customer_errors:
    for error in customer_errors:
        print(error)
else:
    print("Customers data is valid")


# Validate products
product_errors = validate_products(products)

print("\nPRODUCT VALIDATION")

if product_errors:
    for error in product_errors:
        print(error)
else:
    print("Products data is valid")


# Validate sales
sales_errors = validate_sales(sales)

print("\nSALES VALIDATION")

if sales_errors:
    for error in sales_errors:
        print(error)
else:
    print("Sales data is valid")