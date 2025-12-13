from src.features.waiting.infra.resort_storage import ResortStorage
from src.features.waiting.infra.waiting_repository import WaitingRepository


class WaitingSerivice:
    def __init__(self, storage, repository) -> None:
        self.storage: ResortStorage = storage
        self.repository: WaitingRepository = repository

    def get_waiting(self):
        last_update = self.storage.get_last_update()
        items = self.repository.get_by(last_update)
        areas = items.group_by_area()
        return areas.create_response()