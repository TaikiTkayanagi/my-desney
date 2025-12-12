import datetime
import logging
import os
from zoneinfo import ZoneInfo

import boto3
from mypy_boto3_dynamodb import DynamoDBServiceResource
from src.features.resort.modeles.date_time import MyDateTime
from src.features.resort.modeles.resort_place import ResortPlace
from src.features.resort.modeles.resort_url import ResortUrl
from src.features.resort.services.resort_service import ResortService
from src.infrastructures.my_beautifule_soup import MyBeautifuleSoupFactory
from src.infrastructures.my_dynamo_client import MyDynamoClien
from src.infrastructures.my_requests import MyRequests
from src.infrastructures.my_s3_client import MyS3Client



dynamodb: DynamoDBServiceResource = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"]) 
s3 = boto3.client('s3')
logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    logging.info(f'event: {event}')
    now = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
    register_date_time = MyDateTime(now)
    bucket = os.getenv("BUCKET_NAME")
    pt_key = "pt_text/last_update.txt"
    s3_client = MyS3Client(s3, bucket, pt_key)
    land_service = ResortService(MyRequests(), MyBeautifuleSoupFactory(), ResortUrl(True), MyDynamoClien(table), s3_client)
    land_service.save_resort_data(register_date_time, ResortPlace("land"))
    sea_service = ResortService(MyRequests(), MyBeautifuleSoupFactory(), ResortUrl(False), MyDynamoClien(table), s3_client)
    sea_service.save_resort_data(register_date_time, ResortPlace("sea"))
