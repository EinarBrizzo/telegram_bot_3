import requests
import json
from pprint import pprint

TOKEN = "1393764739:AAHdgG7ehkUtXVkN14lzI9E73RRHTuxUrIU"

URL = "https://api.telegram.org/bot{token}/{method}"
# getUpdates - метод для получения обновлений в telegram API
get_updates = "getUpdates"
send = "sendMessage"  # метод для отправки данных. Название метода нужно брать из API
MY_ID = 141756366

WEATHER_TOKEN = "7495abee2a2cb476d274e9d63c18793d"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}"


def get_city(city_data):
    return city_data[0]["message"]["text"]


get_city_url = URL.format(token=TOKEN, method=get_updates)
get_city_text = requests.get(get_city_url).text
get_city_json = json.loads(get_city_text)
get_city_part = get_city_json["result"][::-1]


city = get_city(get_city_part)
pprint(get_city_part[0]["message"]["chat"]["id"])
print(city)

#get_url = URL.format(token=TOKEN, method=get_updates)
get_weather_url = WEATHER_URL.format(city=city, token=WEATHER_TOKEN)


def get_weather_info(weather_data):
    """функция для получения инфо о температуре и вывод инфо в градусах Цельсия """
    return round(weather_data["main"]["temp"] - 273.15)


weather_text = requests.get(get_weather_url).text
weather_json = json.loads(weather_text)

temp = get_weather_info(weather_json)
msg = f"The temperature in {city} is {temp} degrees."

print(msg)


bot_response_url = URL.format(token=TOKEN, method=send)
bot_response_chat_id = get_city_part[0]["message"]["chat"]["id"]
response_msg = {
    "chat_id": bot_response_chat_id,
    "text": msg
}
bot_response_txt = requests.post(bot_response_url, data=response_msg).text

#bot_response_json = json.loads(bot_response_txt)
# print(response_msg)
