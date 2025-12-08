from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://tokyodisneyresort.info/realtime.php?park=sea').text
soup = BeautifulSoup(html_text, "html.parser")
realtime_tags = soup.find_all("div", class_="realtime-attr")
for realtime_tag in realtime_tags:
    name = realtime_tag.find("div", class_="realtime-attr-name")
    time = realtime_tag.find("div", class_="realtime-attr-condition")
    timetable = realtime_tag.find("div", class_="greeting_timetable")

    if name:
        print(name.text)
    if time:
        print(time.text.strip())
    if timetable:
        print(timetable.text)
print(realtime_tag)