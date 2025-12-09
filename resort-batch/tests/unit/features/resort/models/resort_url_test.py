
from src.features.resort.modeles.resort_url import ResortUrl


def test_resort_url_when_land():
    expected1 = "https://tokyodisneyresort.info/realtime.php?park=land&order=area"
    expected2 = "https://tokyodisneyresort.info/greeting_realtime.php?park=land"
    expected3 = "https://tokyodisneyresort.info/restwait.php?park=land"

    
    sut = ResortUrl(isLand=True)

    assert sut.realtime_url_order_by_area() == expected1
    assert sut.greeting_url() == expected2 
    assert sut.restaurants_url() == expected3 

def test_resort_url_when_sea():
    expected1 = "https://tokyodisneyresort.info/realtime.php?park=sea&order=area"
    expected2 = "https://tokyodisneyresort.info/greeting_realtime.php?park=sea"
    expected3 = "https://tokyodisneyresort.info/restwait.php?park=sea"
    
    sut = ResortUrl(isLand=False)

    assert sut.realtime_url_order_by_area() == expected1
    assert sut.greeting_url() == expected2 
    assert sut.restaurants_url() == expected3 