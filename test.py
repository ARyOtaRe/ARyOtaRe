from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint


pp = pprint.PrettyPrinter(indent=4)


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'26',
  'limit':'1',
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
    with open('tests.json', 'w') as file:
      caca=json.dumps(oeuf, indent=2)
      file.write(caca)
#      pp.pprint(oeuf)
      
    
 #   print(oeuf["data"][2]["id"])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  pp.pprint(e)


with open('tests.json', 'r') as file:
    oof = json.loads(file.read())
    pp.pprint(oof["data"][0]["name"])
