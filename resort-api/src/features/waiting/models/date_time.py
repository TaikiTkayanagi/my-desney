from dataclasses import dataclass
import datetime


@dataclass
class MyDateTime:
    _FORMAT = "%Y-%m-%d %H:%M"
    date_time: datetime.datetime 

    def to_str(self) -> str:
        return self.date_time.strftime("%Y-%m-%d %H:%M")

    def before_day(self, day):
        return MyDateTime(self.date_time - datetime.timedelta(days=day))

    def to_minutes_later(self, minutes):
        return MyDateTime(self.date_time + datetime.timedelta(minutes=minutes))

    def to_hour_later(self, hour):
        return MyDateTime(self.date_time + datetime.timedelta(hours=hour))

    @staticmethod
    def create(date_time):
        if date_time is None:
            return None
        return MyDateTime(datetime.datetime.strptime(date_time, MyDateTime._FORMAT))
        
        
        

