import requests
import json

from datetime import timedelta, date

today = date.today()
seven_days = timedelta(days=7)

#weeks = int(input("Count weeks: "))
weeks = 20

for i in range(0, weeks):
  previous_date = today - seven_days
  print(today, previous_date)

  #url ='https://api.nasa.gov/neo/rest/v1/feed?start_date={}&end_date=&api_key=maocFn7G5rQcWIpXRovNX3OQuWJg9ck3jVp9rjt8'.format(previous_date, today)
  #response = requests.get(url)
  #r_json = response.json()
  #print(r_json)
  i = i+1
  for n in range(0,8):
      indays = today - timedelta(days=n)
      print(indays)

  today = previous_date






