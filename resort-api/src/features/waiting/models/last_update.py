from dataclasses import dataclass


@dataclass
class LastUpdate():
    place_time: str
    date_time: str

    def get_place(self):
        return self.place_time.split("_")[0]
    