import random

import requests
import json
import datetime


def random_data(start='2000-01-01'):
    start = datetime.date(*map(int, start.split('-')))
    end = datetime.date.today()
    delta = end - start
    result = str(start + datetime.timedelta(days=random.randint(0, delta.days)))
    return result

API_KEY = "rbw2gqFkwRO0C04wZjwy6DaaNNLbwxeR2IyNoRd9"
data = {'date': random_data(),'api_key':API_KEY}
response = requests.get('https://api.nasa.gov/planetary/apod', params=data)
df = response.json()
print(df)
print(response.status_code)
print(df['explanation'])
print(df["hdurl"])
# if response.status_code == 200:
#     p = requests.get(df['hdurl'])
# else:
#     print('no')