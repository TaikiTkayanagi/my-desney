import asyncio
import logging
import os
import boto3
from mangum import Mangum
from mypy_boto3_dynamodb import DynamoDBServiceResource
from fastapi import FastAPI

from src.features.waiting.services.waiting_service import WaitingSerivice
from src.infrastructures.my_dynamodb_client import MyDynamoDBClient
from src.infrastructures.my_s3_client import MyS3Client


try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

app = FastAPI()
dynamoDb: DynamoDBServiceResource = boto3.resource("dynamodb")
table = dynamoDb.Table(os.environ["TABLE_NAME"])
s3Client = boto3.client("s3")
logger = logging.getLogger()
logger.setLevel("INFO")

@app.get("/land/waiting")
async def land_waiting():
    bucket = os.environ['BUCKET_NAME']
    key = os.environ['LAST_UPDATE_PATH']
    gsi = os.environ['GSI_NAME']
    storage = MyS3Client(s3Client, bucket, key) 
    repository = MyDynamoDBClient(table, gsi)
    return WaitingSerivice("land", storage, repository).get_waiting()

@app.get("/sea/waiting")
async def sea_waiting():
    bucket = os.environ['BUCKET_NAME']
    key = os.environ['LAST_UPDATE_PATH']
    gsi = os.environ['GSI_NAME']
    storage = MyS3Client(s3Client, bucket, key) 
    repository = MyDynamoDBClient(table, gsi)
    return WaitingSerivice("sea", storage, repository).get_waiting()

lambda_handler = Mangum(app, lifespan="off")