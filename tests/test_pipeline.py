import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from extract import read_data


def test_data_extraction():
    customers, products, sales = read_data()

    assert customers is not None
    assert products is not None
    assert sales is not None

from transform import clean_customers


def test_customer_transformation():
    customers, _, _ = read_data()

    cleaned_customers = clean_customers(customers)

    assert cleaned_customers is not None
    assert len(cleaned_customers) > 0

from validate import validate_customers


def test_customer_validation():
    customers, _, _ = read_data()

    errors = validate_customers(customers)

    assert errors is None

from transform import clean_products

def test_product_transformation():
    _, products, _ = read_data()

    cleaned_products = clean_products(products)

    assert cleaned_products is not None
    assert len(cleaned_products) > 0

from transform import clean_sales
def test_sales_transformation():
    _, _, sales = read_data()

    cleaned_sales = clean_sales(sales)

    assert cleaned_sales is not None
    assert len(cleaned_sales) > 0