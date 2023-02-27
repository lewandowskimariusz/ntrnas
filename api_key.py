import requests

basic_url = 'https://api.nasa.gov/'
r = requests.get(basic_url)
print(r)