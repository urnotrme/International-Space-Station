# библиотека для отправки и получения запросов
import requests
# библиотека для открытия url в браузере
import webbrowser
# url api сервера
url = "http://api.open-notify.org/iss-now.json"

# запрос на получение о данных о МКС
rep = requests.get(url)
rep = rep.json()

# получение широты и долготы МКС из ответа сервера
lat = rep["iss_position"]["latitude"]
long = rep["iss_position"]["longitude"]
print("Координаты МКС: ", lat, long)

# запрос в google.maps, координаты передаются как параметры
url_goo = "https://www.google.com/maps/place/{}, {}".format(lat,long)
# открытие google.maps с координатами
webbrowser.open(url_goo)
