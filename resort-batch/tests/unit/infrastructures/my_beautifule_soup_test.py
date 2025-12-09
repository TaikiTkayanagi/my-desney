import pytest
from src.infrastructures.my_beautifule_soup import MyBeautifuleSoup

@pytest.fixture
def html():
    with open("tests/unit/infrastructures/mock.html", "r") as f:
        return f.read()

def test_pick_up_real_time(html):
    sut = MyBeautifuleSoup(html)
    real_times = sut.pick_up_real_time()

    assert real_times.list[0].area == "test1"
    assert real_times.list[0].name == "test2"
    assert real_times.list[0].condition == "test3"

def test_pick_up_greeting(html):
    expected = ["test2", "test5"]

    sut = MyBeautifuleSoup(html)
    greeting = sut.pick_up_greeting()

    assert greeting.names == expected

def test_pick_up_restrant(html):
    expected = ["test2", "test5"]

    sut = MyBeautifuleSoup(html)
    restaurant = sut.pick_up_restrant()

    assert restaurant.names == expected