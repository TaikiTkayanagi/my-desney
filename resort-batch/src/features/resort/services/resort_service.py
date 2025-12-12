import logging
from src.features.resort.infra.resort_requests import ResortRequests
from src.features.resort.infra.resort_html_parser import ResortHtmlParserFactory
from src.features.resort.infra.resort_storage import ResotrStorage
from src.features.resort.infra.waiting_repository import WaitingRepository
from src.features.resort.modeles.date_time import MyDateTime
from src.features.resort.modeles.real_time_entity import GrJson
from src.features.resort.modeles.resort_place import ResortPlace
from src.features.resort.modeles.resort_url import ResortUrl


class ResortService:
    def __init__(self, requests: ResortRequests, factory: ResortHtmlParserFactory, url_creator: ResortUrl, repository: WaitingRepository, storage: ResotrStorage) -> None:
        self.requests = requests
        self.html_parser_factory = factory
        self.url_creator = url_creator
        self.repository = repository
        self.storage = storage
    
    def save_resort_data(self, datetime: MyDateTime, place: ResortPlace) -> None:
        logging.info(f"ResortService: 処理を開始 for {place} at {datetime.to_str()}")
        greeting_names = None
        restrant_names = None
        try:
            if self.storage.is_exist_gr_json(place.get_gr_key()):
                logging.info("S3にgr_jsonが存在するため取得します")
                greeting_names, restrant_names = self.storage.get_gr_names(place.get_gr_key())
        except Exception as e:
            logging.warning(f"S3からのgr_jsonの取得に失敗しました: {e}")
        
        is_gr_save = False
        if greeting_names is None or greeting_names.is_empty():
            logging.info("S3にGreetingが存在しないか、あいまいなため再取得します")
            try:
                greeting_html = self.requests.fetch(self.url_creator.greeting_url())
                greeting_names = self.html_parser_factory.create_parser(greeting_html).pick_up_greeting()
                is_gr_save = True
            except Exception as e:
                logging.error(f"Greetingの取得に失敗しました: {e}")
        if restrant_names is None or restrant_names.is_empty():
            logging.info("S3にRestaurantが存在しないか、あいまいなため再取得します")
            try:
                restrant_html = self.requests.fetch(self.url_creator.restaurants_url())
                restrant_names = self.html_parser_factory.create_parser(restrant_html).pick_up_restrant()
                is_gr_save = True
            except Exception as e:
                logging.error(f"Restaurantの取得に失敗しました: {e}")

        try:
            logging.info("RealTimeを取得します")
            real_time_html = self.requests.fetch(self.url_creator.realtime_url_order_by_area())
            real_times = self.html_parser_factory.create_parser(real_time_html).pick_up_real_time()
        except Exception as e:
            logging.error(f"RealTimeの取得に失敗しました: {e}")
            raise e

        try:
            logging.info("DynamoDBに保存します")
            register = real_times.convert_for_register(greeting_names, restrant_names)
            self.repository.save(register, datetime, place.value)
            self.storage.save_place_time_if_not_cache(datetime.create_time())
        except Exception as e:
            logging.error(f"DynamoDBへの保存に失敗しました: {e}")
            raise e

        if is_gr_save and greeting_names is not None and restrant_names is not None:
            try:
                logging.info("S3にgr_jsonを保存します")
                self.storage.save_gr_json(place.get_gr_key(), GrJson(restaurant=restrant_names, greeting=greeting_names))
            except Exception as e:
                logging.warning(f"S3へのgr_jsonの保存に失敗しました: {e}")
