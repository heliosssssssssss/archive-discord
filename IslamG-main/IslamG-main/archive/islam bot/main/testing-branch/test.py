import requests
from pprint import pprint
import json

r = requests.get(f'https://api.quran.com/api/v4/verses/by_page/5?language=en&words=true&page=1&per_page=1')
x = json.loads(r.text)
pprint(x) 