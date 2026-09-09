def validate_customers(customers):

    errors = []

    #checking missing customer IDs
    missing_customer_ids = customers["customer_id"].isnull().sum()

    if missing_customer_ids > 0:
        errors.append(
            f"Missing Customer IDs: {missing_customer_ids}"

        )

    #check missing customer names
    missing_names = customers["customer_name"].isnull().sum()

    if missing_names > 0:
        errors.append(
            f"Missing Customer Names: {missing_names}"
        )

    #check invalid emaILS

    invalid_emails = customers[
        ~customers["email"].str.contains("@" , na=False)
    ]

    if len(invalid_emails)> 0:
        errors.append(
        f"Invalid Emails: {len(invalid_emails)}"

        )

        return errors


def validate_products(products):

    errors = []

    # Check missing product IDs
    missing_product_ids = products["product_id"].isnull().sum()

    if missing_product_ids > 0:
        errors.append(
            f"Missing Product IDs: {missing_product_ids}"
        )

    # Check invalid prices
    invalid_prices = products[
        (products["price"].isnull()) |
        (products["price"] <= 0)
    ]

    if len(invalid_prices) > 0:
        errors.append(
            f"Invalid Prices: {len(invalid_prices)}"
        )

    # Check invalid stock
    invalid_stock = products[
        (products["stock_quantity"].isnull()) |
        (products["stock_quantity"] < 0)
    ]

    if len(invalid_stock) > 0:
        errors.append(
            f"Invalid Stock Values: {len(invalid_stock)}"
        )

    return errors

def validate_sales(sales):

    errors = []

    # Check missing order IDs
    missing_order_ids = sales["order_id"].isnull().sum()

    if missing_order_ids > 0:
        errors.append(
            f"Missing Order IDs: {missing_order_ids}"
        )

    # Check invalid quantity
    invalid_quantity = sales[
        (sales["quantity"].isnull()) |
        (sales["quantity"] <= 0)
    ]

    if len(invalid_quantity) > 0:
        errors.append(
            f"Invalid Quantity: {len(invalid_quantity)}"
        )

    # Check invalid dates
    invalid_dates = sales[
        sales["order_date"].isnull()
    ]

    if len(invalid_dates) > 0:
        errors.append(
            f"Invalid Dates: {len(invalid_dates)}"
        )

    return errors