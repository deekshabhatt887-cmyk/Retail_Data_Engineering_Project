import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR/"data"/"raw"

def read_data():
    customers = pd.read_csv(
        DATA_PATH / "customers.csv"
    )

    products = pd.read_csv(
        DATA_PATH / "products.csv"
    )

    sales = pd.read_csv(
        DATA_PATH / "sales.csv"
    )

    return customers, products, sales

if __name__ == "__main__":

    customers, products, sales = read_data()

    print("CUSTOMERS DATA")
    print(customers)

    print("\nPRODUCTS DATA")
    print(products)

    print("\nSALES DATA")
    print(sales)