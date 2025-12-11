from dataclasses import asdict
import json
import boto3
from src.features.resort.infra.resort_storage import ResotrStorage
from src.features.resort.modeles.real_time_entity import GrJson, Greeting, Restaurant

s3 = boto3.client('s3')

class MyS3Client(ResotrStorage):
    def __init__(self, bucket, key) -> None:
        self.bucket = bucket
        self.key = key
    
    def is_exist_gr_json(self) -> bool:
        # S3上にgr_jsonが存在するか確認するロジックを実装
        response = s3.list_objects_v2(Bucket=self.bucket, Prefix=self.key)
        return 'Contents' in response

    def get_gr_names(self) -> tuple[Greeting | None , Restaurant | None]:
        response = s3.get_object(Bucket=self.bucket, Key=self.key)
        json_data = json.loads(response['Body'].read().decode('utf-8'))
        g = Greeting(json_data['greeting']['names'])
        r = Restaurant(json_data['restaurant']['names'])
        return g, r

    def save_gr_json(self, gr_json: GrJson) -> None:
        json_data = json.dumps(asdict(gr_json)).encode('utf-8') 
        s3.put_object(
            Bucket=self.bucket,
            Key=self.key,
            Body=json_data
        )