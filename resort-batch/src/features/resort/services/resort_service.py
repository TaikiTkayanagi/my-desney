from src.features.resort.infra.resort_requests import ResortRequests
from src.features.resort.infra.resort_html_parser import ResortHtmlParserFactory
from src.features.resort.infra.resort_storage import ResotrStorage
from src.features.resort.infra.waiting_repository import WaitingRepository
from src.features.resort.modeles.real_time_entity import GrJson
from src.features.resort.modeles.resort_url import ResortUrl


class ResortService:
    def __init__(self, requests: ResortRequests, factory: ResortHtmlParserFactory, url_creator: ResortUrl, repository: WaitingRepository, storage: ResotrStorage) -> None:
        self.requests = requests
        self.html_parser_factory = factory
        self.url_creator = url_creator
        self.repository = repository
        self.storage = storage
    
    def save_resort_data(self, datetime: str, place: str) -> None:
        greeting_names = None
        restrant_names = None
        if self.storage.is_exist_gr_json():
            greeting_names, restrant_names = self.storage.get_gr_names()
        
        is_gr_save = False
        if greeting_names is None or greeting_names.is_empty():
            greeting_html = self.requests.fetch(self.url_creator.greeting_url())
            greeting_names = self.html_parser_factory.create_parser(greeting_html).pick_up_greeting()
            is_gr_save = True
        if restrant_names is None or restrant_names.is_empty():
            restrant_html = self.requests.fetch(self.url_creator.restaurants_url())
            restrant_names = self.html_parser_factory.create_parser(restrant_html).pick_up_restrant()
            is_gr_save = True

        real_time_html = self.requests.fetch(self.url_creator.realtime_url_order_by_area())
        real_times = self.html_parser_factory.create_parser(real_time_html).pick_up_real_time()

        register = real_times.convert_for_register(greeting_names, restrant_names)
        self.repository.save(register, datetime, place)

        if is_gr_save:
            self.storage.save_gr_json(GrJson(restaurant=restrant_names, greeting=greeting_names))
