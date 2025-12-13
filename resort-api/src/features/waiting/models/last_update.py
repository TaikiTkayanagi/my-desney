from dataclasses import dataclass


@dataclass
class LastUpdate():
    value: str

    def create_place_time(self, place: str):
        return f"{place}-{self.value}"
    