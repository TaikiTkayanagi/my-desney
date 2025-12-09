from src.features.resort.infra.resort_requests import ResortRequests
from src.features.resort.infra.resort_html_parser import ResortHtmlParserFactory
from src.features.resort.modeles.resort_url import ResortUrl


class ResortService:
    def __init__(self, resort_requests: ResortRequests, html_parser_factory: ResortHtmlParserFactory, url_creator: ResortUrl) -> None:
        self.requests = resort_requests
        self.html_parser_factory = html_parser_factory
        self.url_creator = url_creator
    
    def save_resort_data(self):
        greeting_html = self.requests.fetch(self.url_creator.greeting_url())
        restrant_html = self.requests.fetch(self.url_creator.restaurants_url())
        real_time_html = self.requests.fetch(self.url_creator.realtime_url_order_by_area())
        greeting_names = self.html_parser_factory.create_parser(greeting_html).pick_up_greeting()
        restrant_names = self.html_parser_factory.create_parser(restrant_html).pick_up_restrant()
        real_times = self.html_parser_factory.create_parser(real_time_html).pick_up_real_time()
        register = real_times.convert_for_register(greeting_names, restrant_names)
