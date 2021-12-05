import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':'6892',
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
    print(oeuf["data"]["6892"]["name"])

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)



def current(args=str):
  """Shows the weather information of the city of your choice!"""
  print("it's a me!")
  try:
    cmoplete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+f"{args}"+"&appid=6e2d2db27e5a42fa384a698d859fc686"
    api_link=requests.get(cmoplete_api_link)
    api_data=api_link.json()
    print(cmoplete_api_link)
  except requests.exceptions.RequestException as e:
    print(e)
  if api_data['cod']=='404':
    print("hey fuck off that's not the right city")
  else:
    temperature=((api_data['main']['temp'])-273.15)
    windspeed=((api_data['wind']['speed'])*3.6)
    city = f'{args}\'' if args[-1]=='s' else f'{args}\'s'
    fahr=9.0/5.0 * temperature + 32
    print(f"{temperature}°C and {fahr}F")
  print(city)


current("Guérande")
