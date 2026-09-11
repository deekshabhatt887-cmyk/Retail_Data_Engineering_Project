import pandas as pd
from io import BytesIO
from minio import Minio


# Connect to MinIO
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin123",
    secure=False
)

BUCKET_NAME = "retail-data"


def read_csv_from_minio(file_name):
    response = client.get_object(
        BUCKET_NAME,
        f"raw/{file_name}"
    )

    data = response.read()

    response.close()
    response.release_conn()

    return pd.read_csv(BytesIO(data))


def read_data():
    customers = read_csv_from_minio("customers.csv")
    products = read_csv_from_minio("products.csv")
    sales = read_csv_from_minio("sales.csv")

    return customers, products, sales


if __name__ == "__main__":

    customers, products, sales = read_data()

    print("CUSTOMERS DATA")
    print(customers)

    print("\nPRODUCTS DATA")
    print(products)

    print("\nSALES DATA")
    print(sales)