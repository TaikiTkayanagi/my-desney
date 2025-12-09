class ResortUrl:
    BASE_URL = "https://tokyodisneyresort.info"

    def __init__(self, isLand: bool) -> None:
        self.kind = isLand and "land" or "sea"

    def realtime_url_order_by_area(self) -> str:
        return f"{self.BASE_URL}/realtime.php?park={self.kind}&order=area"

    def greeting_url(self) -> str:
        return f"{self.BASE_URL}/greeting_realtime.php?park={self.kind}"

    def restaurants_url(self) -> str:
        return f"{self.BASE_URL}/restwait.php?park={self.kind}"
    