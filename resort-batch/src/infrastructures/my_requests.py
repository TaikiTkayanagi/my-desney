from requests import Session
import requests

from src.features.resort.infra.resort_requests import ResortRequests


class MyRequests(ResortRequests):
    def __init__(self) -> None:
        self.my_requests: Session = requests.Session() 

    def fetch(self, url: str) -> str:
        response = self.my_requests.get(url)
        return response.text
