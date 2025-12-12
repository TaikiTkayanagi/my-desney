from dataclasses import asdict
import json
from mypy_boto3_s3 import S3Client
from src.features.resort.infra.resort_storage import ResotrStorage
from src.features.resort.modeles.real_time_entity import GrJson, Greeting, Restaurant


class MyS3Client(ResotrStorage):
    def __init__(self, s3: S3Client, bucket, pt_text_key) -> None:
        self.s3 = s3
        self.bucket = bucket
        self.pt_text_key = pt_text_key
        self.save_update_time_cache = False
    
    def is_exist_gr_json(self, gr_json_key: str) -> bool:
        response = self.s3.list_objects_v2(Bucket=self.bucket, Prefix=gr_json_key)
        return 'Contents' in response

    def get_gr_names(self, gr_json_key: str) -> tuple[Greeting | None , Restaurant | None]:
        response = self.s3.get_object(Bucket=self.bucket, Key=gr_json_key)
        json_data = json.loads(response['Body'].read().decode('utf-8'))
        g = Greeting(json_data['greeting']['names'])
        r = Restaurant(json_data['restaurant']['names'])
        return g, r

    def save_gr_json(self, gr_json_key, gr_json: GrJson) -> None:
        json_data = json.dumps(asdict(gr_json), ensure_ascii=False).encode('utf-8') 
        self.s3.put_object(
            Bucket=self.bucket,
            Key=gr_json_key,
            Body=json_data
        )
    
    def save_place_time_if_not_cache(self, date_time: str) -> None:
        if self.save_update_time_cache:
            return

        self.s3.put_object(
            Bucket=self.bucket,
            Key=self.pt_text_key,
            Body=date_time.encode('utf-8')
        )
        self.save_update_time_cache = True
