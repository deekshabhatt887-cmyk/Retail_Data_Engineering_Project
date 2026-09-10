from extract import read_data
from transform import(
    clean_customers,
    clean_products,
    clean_sales
)

customers, products, sales = read_data()

cleaned_customers = clean_customers(customers)
cleaned_products = clean_products(products)
cleaned_sales = clean_sales(sales)

print("CLEANED CUSTOMERS")
print(cleaned_customers)

print("\nCLEANED PRODUCTS")
print(cleaned_products)

print("\nCLEANED  SALES")
print(cleaned_sales)