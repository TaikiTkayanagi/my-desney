from boto3.dynamodb.conditions import Key
from mypy_boto3_dynamodb.service_resource import Table
from src.features.waiting.infra.waiting_repository import WaitingRepository
from src.features.waiting.models.last_update import LastUpdate
from src.features.waiting.models.waiting_item import WaitingItem, WaitingItems


class MyDynamoDBClient(WaitingRepository):
    def __init__(self, table: Table, gsi:str):
        self.table = table
        self.gsi = gsi

    def get_by(self, date_time: str, place: str) -> WaitingItems:
        response = self.table.query(
            IndexName=self.gsi,
            KeyConditionExpression=Key("date_time").eq(date_time) & Key("place").eq(place),
            ReturnConsumedCapacity="TOTAL",
            ConsistentRead=False
        )

        ret = []
        for item in response["Items"]:
            ret.append(
                WaitingItem(
                    place_time=str(item['place_time']),
                    id=str(item['id']),
                    area=str(item['area']),
                    condition=str(item['condition']),
                    date_time=str(item['date_time']),
                    name=str(item['name']),
                    place=str(item['place']),
                    type=str(item['type'])
                )
            )
        
        return WaitingItems(ret)
