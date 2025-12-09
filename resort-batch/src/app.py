import json

import requests

from src.features.resort.services.resort_service import ResortService
from src.infrastructures.my_beautifule_soup import MyBeautifuleSoupFactory
from src.infrastructures.my_requests import MyRequests


# import requests


#def lambda_handler(event, context):
    #service = ResortService(MyRequests(), MyBeautifuleSoupFactory())
    #service.save_resort_data()
