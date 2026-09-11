from minio import Minio


client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin123",
    secure=False
)


buckets = client.list_buckets()

print("Connected to MinIO successfully!")

for bucket in buckets:
    print("Bucket:", bucket.name)