from src.services.resort_service.resort_html_parser import ResortHtmlParserFactory
from src.services.resort_service.resort_requests import ResortRequests


class ResortService:
    def __init__(self, resort_requests: ResortRequests, html_parser_factory: ResortHtmlParserFactory) -> None:
        self.requests = resort_requests
        self.html_parser_factory = html_parser_factory
    
    def save_resort_data(self):
        url = 'https://tokyodisneyresort.info/realtime.php?park=sea'
        html_text = self.requests.fetch_html_text(url)
        parser = self.html_parser_factory.create_parser(html_text)
        parser.pick_up_realtimes()
