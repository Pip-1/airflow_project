import pandas as pd
from datetime import datetime
import json
import requests

access_key = "2d90d10eae259b217aee8119adc6ae70"

#creating variable to pass todays date to the API
today = datetime.today()
city = "Erfurt"

#creating variable for the response from the API
#response.text would output the response from the API
response_weather = requests.get("http://api.weatherstack.com/current?access_key=2d90d10eae259b217aee8119adc6ae70&query={city}")

# Parse the JSON data
current_weather_data_raw = json.loads(response_weather.text)

city_name = data['location']['name']
country = data['location']['country']
local_time = data['location']['localtime']
temperature = data['current']['temperature']
weather_description = data['current']['weather_descriptions'][0]

