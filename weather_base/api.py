import requests


class Api(object):
    def __init__(self):
        self.key = "89055558a0d4f266d3213909268cb9a9"

    def Get_weather(self, city):
        weather_keys = ["description", "icon"]
        temp_keys = ["temp", "temp_min", "temp_max", "humidity"]
        self.base = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={self.key}"
        self.req = requests.get(self.base).json()
        for weather in self.req.get("weather"):
            if "sky" in list(map(weather.get, weather_keys))[0]:
                val_1 = f"Description : {list(map(weather.get, weather_keys))[0]}\n Condition : 盛 "
            elif "clouds" in list(map(weather.get, weather_keys))[0]:
                val_1 = f"Description : {list(map(weather.get, weather_keys))[0]}\n Condition :  "
            elif "rain" in list(map(weather.get, weather_keys))[0]:
                val_1 = f"Description : {list(map(weather.get, weather_keys))[0]}\n Condition :   "
            elif "thunderstorm" in list(map(weather.get, weather_keys))[0]:
                val_1 = f"Description : {list(map(weather.get, weather_keys))[0]}\n Condition :   "
            elif "snow" in list(map(weather.get, weather_keys))[0]:
                val_1 = f"Description : {list(map(weather.get, weather_keys))[0]}\n Condition :  "

        for temp in ([self.req.get("main")]):
            val_2 = f"Temperature :{list(map(temp.get, temp_keys))[0]}°C\nMin Temperature :{list(map(temp.get, temp_keys))[1]}°C\nMax Temperature :{list(map(temp.get, temp_keys))[2]}°C"
            return f"{val_1}\n{val_2}"
