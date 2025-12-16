from dataclasses import dataclass
import datetime

from src.features.waiting.models.date_time import MyDateTime


@dataclass
class LastUpdate():
    date_time: str