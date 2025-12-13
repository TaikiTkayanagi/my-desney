
from mypy_boto3_s3 import S3Client
from src.features.waiting.infra.resort_storage import ResortStorage
from src.features.waiting.models.last_update import LastUpdate


class MyS3Client(ResortStorage):
    def __init__(self, client: S3Client, bucket: str, key: str) -> None:
        self.client = client 
        self.bucket = bucket
        self.key = key
    
    def get_last_update(self):
        res = self.client.get_object(Bucket=self.bucket, Key=self.key)
        body = res['Body'].read().decode('utf-8')
        return LastUpdate(body)
