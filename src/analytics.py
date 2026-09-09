from database import get_engine
import pandas as pd


def get_total_sales(start_date, end_date):

    engine = get_engine()

    query = """
        SELECT
            SUM(s.quantity * p.price) AS total_sales
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        WHERE s.order_date >= %(start_date)s
          AND s.order_date < %(end_date)s + INTERVAL '1 day'
    """

    result = pd.read_sql(
        query,
        engine,
        params={
            "start_date": start_date,
            "end_date": end_date
        }
    )

    engine.dispose()

    return result

def get_top_selling_products(start_date, end_date):

    engine = get_engine()

    query = """
        SELECT
            p.product_name,
            SUM(s.quantity) AS total_quantity_sold
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        WHERE s.order_date >= %(start_date)s
          AND s.order_date < %(end_date)s + INTERVAL '1 day'
        GROUP BY p.product_name
        ORDER BY total_quantity_sold DESC
    """

    result = pd.read_sql(
        query,
        engine,
        params={
            "start_date": start_date,
            "end_date": end_date
        }
    )

    engine.dispose()

    return result
def get_sales_by_city(start_date, end_date):

    engine = get_engine()

    query = """
        SELECT
            c.city,
            SUM(s.quantity * p.price) AS total_sales
        FROM sales AS s
        JOIN customers AS c
            ON s.customer_id = c.customer_id
        JOIN products AS p
            ON s.product_id = p.product_id
        WHERE s.order_date >= %(start_date)s
          AND s.order_date < %(end_date)s + INTERVAL '1 day'
        GROUP BY c.city
        ORDER BY total_sales DESC
    """

    result = pd.read_sql(
        query,
        engine,
        params={
            "start_date": start_date,
            "end_date": end_date
        }
    )

    engine.dispose()

    return result
def get_monthly_sales(start_date, end_date):

    engine = get_engine()

    query = """
        SELECT
            DATE_TRUNC('month', s.order_date) AS month,
            SUM(s.quantity * p.price) AS total_sales
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        WHERE s.order_date >= %(start_date)s
          AND s.order_date < %(end_date)s + INTERVAL '1 day'
        GROUP BY month
        ORDER BY month
    """

    result = pd.read_sql(
        query,
        engine,
        params={
            "start_date": start_date,
            "end_date": end_date
        }
    )

    engine.dispose()

    return result

def get_top_customers():
    engine = get_engine()

    query = """
        SELECT
            c.customer_name,
            c.city,
            SUM(s.quantity * p.price) AS total_spent
        FROM sales AS s
        JOIN customers AS c
            ON s.customer_id = c.customer_id
        JOIN products AS p
            ON s.product_id = p.product_id
        GROUP BY c.customer_name, c.city
        ORDER BY total_spent DESC
    """

    result = pd.read_sql(query, engine)

    engine.dispose()
    return result



def get_dashboard_summary(start_date, end_date):

    engine = get_engine()

    query = """
        SELECT
            COALESCE(SUM(s.quantity * p.price), 0) AS total_sales,
            COALESCE(SUM(s.quantity), 0) AS total_units_sold,
            COUNT(DISTINCT s.customer_id) AS total_customers,
            COUNT(DISTINCT s.product_id) AS products_sold
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        WHERE s.order_date >= %(start_date)s
          AND s.order_date < %(end_date)s + INTERVAL '1 day'
    """

    result = pd.read_sql(
        query,
        engine,
        params={
            "start_date": start_date,
            "end_date": end_date
        }
    )

    engine.dispose()

    return result