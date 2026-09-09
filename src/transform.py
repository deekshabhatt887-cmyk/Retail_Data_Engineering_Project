import pandas as pd

def clean_customers(customers):
    #remove duplicate customers

    customers = customers.drop_duplicates()

    #remove extra spaces
    customers["customer_name"] = customers["customer_name"].str.strip()

    #capitalixe name
    customers["customer_name"] = customers["customer_name"].str.title()

    #email to lowercase
    customers["email"] = customers["email"].str.lower()

    #clean city names
    customers["city"] = customers["city"].str.strip().str.title()

    return customers

def clean_products(products):

     # Remove duplicate products
    products = products.drop_duplicates()

    # Remove extra spaces
    products["product_name"] = products["product_name"].str.strip()

    # Standardize product names
    products["product_name"] = products["product_name"].str.title()

    # Standardize category
    products["category"] = products["category"].str.strip().str.title()

#convert price to numeric
    products["price"] = pd.to_numeric(
        products["price"],
        errors= "coerce"
    )

    return products

def clean_sales(sales):

    # Remove duplicate sales
    sales = sales.drop_duplicates()

    # Convert quantity to numeric
    sales["quantity"] = pd.to_numeric(
        sales["quantity"],
        errors="coerce"
    )

    # Convert order date to datetime
    sales["order_date"] = pd.to_datetime(
        sales["order_date"],
        errors="coerce"
    )

    # Clean store names
    sales["store"] = sales["store"].str.strip().str.title()

    return sales