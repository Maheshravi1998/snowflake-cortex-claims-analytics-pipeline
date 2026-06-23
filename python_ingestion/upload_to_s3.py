import boto3
from pathlib import Path

BUCKET_NAME = "your-s3-bucket-name"
LOCAL_FILE = Path("data/sample_claims_data.csv")
S3_KEY = "claims/sample_claims_data.csv"

def upload_file_to_s3():
    s3_client = boto3.client("s3")

    s3_client.upload_file(
        Filename=str(LOCAL_FILE),
        Bucket=BUCKET_NAME,
        Key=S3_KEY
    )

    print(f"Uploaded {LOCAL_FILE} to s3://{BUCKET_NAME}/{S3_KEY}")

if __name__ == "__main__":
    upload_file_to_s3()
