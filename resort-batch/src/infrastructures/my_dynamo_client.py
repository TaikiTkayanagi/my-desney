
from typing import List

from mypy_boto3_dynamodb import DynamoDBServiceResource
from mypy_boto3_dynamodb.service_resource import Table
from src.features.resort.infra.waiting_repository import WaitingRepository
from src.features.resort.modeles.real_time_entity import RegisterRealTime


class MyDynamoClien(WaitingRepository):
    def __init__(self, table: Table) -> None:
        self.table = table
    
    def save(self, register: List[RegisterRealTime], datetime: str, place: str) -> None:
        with self.table.batch_writer() as batch:
            for item in register:
                batch.put_item(Item={
                    'date_time': datetime,
                    'name': item.name,
                    'area': item.area,
                    'type': item.type,
                    'condition': item.condition,
                    'place': place
                })
    