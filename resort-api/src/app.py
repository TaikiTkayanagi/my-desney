import os
import boto3
from boto3.dynamodb.conditions import Key
from mypy_boto3_dynamodb import DynamoDBServiceResource
from fastapi import FastAPI

from src.features.waiting.services.waiting_service import WaitingSerivice
from src.infrastructures.my_dynamodb_client import MyDynamoDBClient
from src.infrastructures.my_s3_client import MyS3Client



app = FastAPI()
dynamoDb: DynamoDBServiceResource = boto3.resource("dynamodb")
table = dynamoDb.Table(os.environ["TABLE_NAME"])
s3Client = boto3.client("s3")

@app.get("/land/waiting")
async def land_waiting():
    bucket = os.environ['BUCKET_NAME']
    key = os.environ['LAST_UPDATE_PATH']
    storage = MyS3Client(s3Client, bucket, key) 
    repository = MyDynamoDBClient(table)
    return WaitingSerivice(storage, repository).get_waiting()
