from dataclasses import dataclass
from datetime import datetime, timedelta



@dataclass
class MyDateTime:
    value: datetime

    def to_str(self) -> str:
        return self.value.strftime("%Y-%m-%d %H:%M")
    
    def create_place_time(self, place: str) -> str:
        # IDは場所と年月日時とする
        # 年月日時分まで含めると、特定時間の予測を出す際DynamoDBの取得を複数回行う必要があるため、時間までとする
        return f"{place}-{self.create_time()}"
    
    def create_time(self) -> str:
        return self.value.strftime('%Y%m%d%H')