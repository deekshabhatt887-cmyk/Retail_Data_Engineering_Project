from database import get_connection


# ---------------------------------
# LOAD CUSTOMERS
# ---------------------------------

def load_customers(customers):

    # Connect to PostgreSQL
    connection = get_connection()

    # Create cursor
    cursor = connection.cursor()

    # SQL query
    query = """
        INSERT INTO customers
        (customer_id, customer_name, email, city, state)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (customer_id)
        DO UPDATE SET
           customer_name = EXCLUDED.customer_name,
           email = EXCLUDED.email,
           city = EXCLUDED.city,
           state = EXCLUDED.state

    """

    # Loop through every customer
    for _, row in customers.iterrows():

        cursor.execute(
            query,
            (
                int(row["customer_id"]),
                row["customer_name"],
                row["email"],
                row["city"],
                row["state"]
            )
        )

    # Save changes
    connection.commit()

    # Close connection
    cursor.close()
    connection.close()

    print("Customers loaded successfully!")


# ---------------------------------
# LOAD PRODUCTS
# ---------------------------------

def load_products(products):

    # Connect to PostgreSQL
    connection = get_connection()

    # Create cursor
    cursor = connection.cursor()

    # SQL query
    query = """
        INSERT INTO products
        (product_id, product_name, category, price, stock_quantity)
        VALUES (%s, %s, %s, %s, %s)

        ON CONFLICT (product_id)
        DO UPDATE SET
           product_name = EXCLUDED.product_name,
           category = EXCLUDED.category,
           price = EXCLUDED.price,
           stock_quantity = EXCLUDED.stock_quantity
    """

    # Loop through every product
    for _, row in products.iterrows():

        cursor.execute(
            query,
            (
                int(row["product_id"]),
                row["product_name"],
                row["category"],
                float(row["price"]),
                int(row["stock_quantity"])
            )
        )

    # Save changes
    connection.commit()

    # Close connection
    cursor.close()
    connection.close()

    print("Products loaded successfully!")


# ---------------------------------
# LOAD SALES
# ---------------------------------

def load_sales(sales):

    # Connect to PostgreSQL
    connection = get_connection()

    # Create cursor
    cursor = connection.cursor()

    # SQL query
    query = """
        INSERT INTO sales
        (order_id, customer_id, product_id, quantity, order_date, store)
        VALUES (%s, %s, %s, %s, %s, %s)  

        ON CONFLICT (order_id)
        DO UPDATE SET
            customer_id = EXCLUDED.customer_id,
            product_id = EXCLUDED.product_id,
            quantity = EXCLUDED.quantity,
            order_date = EXCLUDED.order_date,
            store = EXCLUDED.store
    """

    # Loop through every sale
    for _, row in sales.iterrows():

        cursor.execute(
            query,
            (
                int(row["order_id"]),
                int(row["customer_id"]),
                int(row["product_id"]),
                int(row["quantity"]),
                row["order_date"],
                row["store"]
            )
        )

    # Save changes
    connection.commit()

    # Close connection
    cursor.close()
    connection.close()

    print("Sales loaded successfully!")