from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
"""
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a80e718a-61fa-4358-80c0-14b3cbcae1bd',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    oeuf = json.loads(response.text)
    #with open('test.json', 'w') as file:
    #    caca=json.dumps(data, indent=2)
    #    file.write(caca)
    #print(data)
    
    print(oeuf["data"][2]["id"])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
"""

with open('test.json', 'r') as file:
    #caca=json.dumps(data, indent=2)
    #file.write(caca)
    #print(data)
    oeuf = json.loads(file.read())
    
    print(oeuf["data"][22])