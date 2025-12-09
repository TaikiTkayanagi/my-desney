
from typing import List

import boto3
from mypy_boto3_dynamodb import DynamoDBServiceResource
from src.features.resort.infra.waiting_repository import WaitingRepository
from src.features.resort.modeles.real_time_entity import RegisterRealTime

dynamodb: DynamoDBServiceResource = boto3.resource('dynamodb')
table = dynamodb.Table("WaitingResortTable") 

class MyDynamoClien(WaitingRepository):
    def save(self, register: List[RegisterRealTime], datetime: str, place: str) -> None:
        with table.batch_writer() as batch:
            for item in register:
                batch.put_item(Item={
                    'date_time': datetime,
                    'name': item.name,
                    'area': item.area,
                    'type': item.type,
                    'condition': item.condition,
                    'place': place
                })
    