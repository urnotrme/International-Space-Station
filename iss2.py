import requests
from time import sleep as sp
import webbrowser as wb

url = 'http://api.open-notify.org/iss-now.json'

while True:
    a = requests.get(url)
    a = a.json()

    position = a["iss_position"]
    latitude = a["iss_position"]["latitude"]
    longitude = a["iss_position"]["longitude"]

    print(latitude, longitude)

    url_google = 'https://www.google.ru/maps/place/{},{}'.format(latitude, longitude)
    wb.open(url_google)

    sp(60)
