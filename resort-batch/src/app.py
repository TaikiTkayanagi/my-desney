import datetime
import os

import boto3
from mypy_boto3_dynamodb import DynamoDBServiceResource
from src.features.resort.modeles.resort_url import ResortUrl
from src.features.resort.services.resort_service import ResortService
from src.infrastructures.my_beautifule_soup import MyBeautifuleSoupFactory
from src.infrastructures.my_dynamo_client import MyDynamoClien
from src.infrastructures.my_requests import MyRequests
from src.infrastructures.my_s3_client import MyS3Client



dynamodb: DynamoDBServiceResource = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["TABLE_NAME"]) 

def lambda_handler(event, context):
    print(f'event: {event}')
    
    now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9)))
    register_date_time = now.strftime("%Y-%m-%d %H:%M")
    bucket = os.getenv("BUCKET_NAME")
    land_key = "gr_json/land_gr_json.json"
    sea_key = "gr_json/sea_gr_json.json"
    land_service = ResortService(MyRequests(), MyBeautifuleSoupFactory(), ResortUrl(True), MyDynamoClien(table), MyS3Client(bucket, land_key))
    land_service.save_resort_data(register_date_time, "land")
    sea_service = ResortService(MyRequests(), MyBeautifuleSoupFactory(), ResortUrl(True), MyDynamoClien(table), MyS3Client(bucket, sea_key))
    sea_service.save_resort_data(register_date_time, "sea")
