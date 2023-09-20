import pandas as pd
from datetime import datetime
import json
import requests
from api_creds import access_key

#creating variable to pass todays date to the API
timestamp = datetime.now()
city = "Erfurt"

#creating variable for the response from the API
#response.text would output the response from the API
response_weather = requests.get(f"http://api.weatherstack.com/current?access_key={access_key}&query={city}")

# Parse the JSON data
current_weather_data_raw = json.loads(response_weather.text)

# Creating a dictionary to prepare the data for the dataframe
data_dict = {
    'timestamp_etl': [timestamp],
    'local_time': [current_weather_data_raw['location']['localtime']],
    'city': [current_weather_data_raw['location']['name']],
    'country': [current_weather_data_raw['location']['country']],
    'temp_in_c': [current_weather_data_raw['current']['temperature']],
    'weather_desc': [current_weather_data_raw['current']['weather_descriptions'][0]],
}

# Creating a dataframe
weather_df = pd.DataFrame(data_dict)

weather_df.to_csv('weather_data.csv', index=False)

