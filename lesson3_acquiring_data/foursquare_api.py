import os
import json
import requests

url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
    client_id=os.environ['FOURSQUARE_ID'],
    client_secret=os.environ['FOURSQUARE_SECRET'],
    v='20180323',
    near='Seattle, WA',
    # query='coffee',
    limit=10,
    time='any',
    day='any',
    offset=3  # pages of results
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
# print(data.keys())
# print(data['response'].keys())
# print(data['response']['totalResults'])
# print(data['response']['groups'][0]['items'])
# print(data['response']['groups'][0])

names = [v['venue']['name'] for v in data['response']['groups'][0]['items']]
for name in names:
    print('- ' + name)

# print(data['response']['groups'][0]['items'][0])
