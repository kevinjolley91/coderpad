import requests
import os

class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()
        
    def get_data(self):
        
        apikey = os.environ.get('WEATHER_API_KEY')
        
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&units={self.units}&appid={apikey}")

        except:
            print("No internet access :(")
    

        response_json = response.json()

        self.temp = response_json["main"]["temp"]
        self.feels_like = response_json["main"]["feels_like"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]
        
    def temp_print(self):
        units_symbol = "F"
        if self.units == "metric":
            units_symbol = "C"
        print(f"In {self.name}, it is {self.temp}° {units_symbol}, but feels like {self.feels_like}° {units_symbol}.")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")
        print(f"Today's High: {self.temp_max}° {units_symbol}")
        
        

my_city = City("Franklin", 41.4115, -79.8521)
my_city.temp_print()

vacation_city = City("Pittsburgh", 40.4406, -79.9959, "metric")
vacation_city.temp_print()