import pandas as pd
from datetime import datetime
import requests

access_key = "2d90d10eae259b217aee8119adc6ae70"

#creating variable to pass todays date to the API
today = datetime.today().strftime("%m/%d")

#creating variable for the response from the API
response = requests.get(f"http://numbersapi.com/{today}/date")

#response.text would output the response from the API
