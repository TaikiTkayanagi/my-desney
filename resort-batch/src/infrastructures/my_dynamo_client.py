
from typing import List
import uuid

from mypy_boto3_dynamodb.service_resource import Table
from src.features.resort.infra.waiting_repository import WaitingRepository
from src.features.resort.modeles.date_time import MyDateTime
from src.features.resort.modeles.real_time_entity import RegisterRealTime


class MyDynamoClien(WaitingRepository):
    def __init__(self, table: Table) -> None:
        self.table = table
    
    def save(self, register: List[RegisterRealTime], datetime: MyDateTime, place: str) -> None:
        with self.table.batch_writer() as batch:
            for item in register:
                batch.put_item(Item={
                    'place_time': datetime.create_place_time(place),
                    'id': str(uuid.uuid4()),
                    'date_time': datetime.to_str(),
                    'name': item.name,
                    'area': item.area,
                    'type': item.type,
                    'condition': item.condition,
                    'place': place
                })
    