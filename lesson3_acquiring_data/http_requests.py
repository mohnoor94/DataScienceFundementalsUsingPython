# 'requests' Docs: http://docs.python-requests.org/en/master/

import requests
from bs4 import BeautifulSoup  # for xml

# res = requests.get('https://www.nytimes.com')
#
# print(res)
# print(res.status_code)
# print(res.url)
# print(res.request)
# print(res.headers)
# print(res.ok)
# print(res.text)  # full page source

jsonRes = requests.get('https://data.sfgov.org/resource/wwmu-gmzc.json')
# print(res.text)
# print(res.json())  # gives a python dictionary out of the json object (a list of dicts)
# print(type(res.text))
# print(type(res.json()))
# print(type(res.json()[0]))
# print(jsonRes.json()[0])
# print(jsonRes.json()[0]['release_year'])


xmlRes = requests.get('https://data.sfgov.org/resource/wwmu-gmzc.xml')
# print(xmlRes.text)

soup = BeautifulSoup(xmlRes.text, 'html.parser')
# print(soap.prettify())
# print(soup.rows)

# for row in soup.rows:
#     print(row.title)

# print(list(soup.rows.children))
# print(len(list(soup.rows.children)))

print(soup.find('row'))
print(len(soup.find_all('row')))

print(soup.find(_id="row-m99r~gea6_qnzc"))  # attribute of a row
