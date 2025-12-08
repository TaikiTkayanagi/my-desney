import json

import requests

from src.infrastructures.my_requests import MyRequests
from src.services.resort_service.resort_service import ResortService


# import requests


def lambda_handler(event, context):
    service = ResortService(MyRequests())
    service.save_resort_data()
