import datetime
import logging
from typing import Union

from src.features.waiting.infra.resort_storage import ResortStorage
from src.features.waiting.infra.waiting_repository import WaitingRepository
from src.features.waiting.models.date_time import MyDateTime


class WaitingSerivice:
    def __init__(self, place: str, storage, repository) -> None:
        self.place = place
        self.storage: ResortStorage = storage
        self.repository: WaitingRepository = repository

    def get_waiting(self, date_time: Union[None, MyDateTime]):
        logging.info(f"{self.place}のwaiting取得開始")
        try:
            if date_time is None:
                last_update = self.storage.get_last_update()
                date_time = MyDateTime.create(last_update.date_time)
            if date_time is None:
                raise Exception("last_updateの中身が異常です")
            items = self.repository.get_by(date_time.to_str(), self.place)
            items_30_minutes_later = self.repository.get_by(date_time.before_day(1).to_minutes_later(30).to_str(), self.place).pick_up_name_condition()
            items_1_hours_later = self.repository.get_by(date_time.before_day(1).to_hour_later(1).to_str(), self.place).pick_up_name_condition()
            items_3_hours_later = self.repository.get_by(date_time.before_day(1).to_hour_later(3).to_str(), self.place).pick_up_name_condition()
            areas = items.group_by_area(items_30_minutes_later, items_1_hours_later, items_3_hours_later)
            return areas.create_response()
        except Exception as e:
            logging.error(f'例外発生: {e}')
            raise e
        