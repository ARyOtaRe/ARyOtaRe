import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import random
import time
import urllib3
import tkinter as tk
import tkinter.font as font 
from cv2 import cv2
import numpy as np

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

with open("tests.json", "w") as f:
  f.write(json.dumps(oeuf, indent=2))

"""

def current(args=str):
  
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
"""

with open("C:\\Users\\ARyOtaRe\\Documents\\SlashBot\\en.json", encoding="utf8") as en_json:
  en_data=json.loads(en_json.read())

with open("C:\\Users\\ARyOtaRe\\Documents\\SlashBot\\fr.json", encoding="utf8") as fr_json:
  fr_data=json.loads(fr_json.read())
template_data={}

for key in en_data:
  if key not in fr_data:
    print(f"\"{key}\": \"\",")

print("\n\n")

data={}
for key, value in en_data.items():
  if key in data:
    print(f'"{key}": "{value}",')

"""


def main():
  vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)

  if vc.isOpened():
    rval, frame = vc.read()
  else:
    rval = False

  while rval:
    rval, frame = vc.read()
    print(toASCII(frame))

    key = cv2.waitKey(50) # 50ms pause -> ~20fps
    # Press echap to end
    if key == 27:
      break

def toASCII(frame, cols = 120, rows = 35):

  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  height, width = frame.shape
  cell_width = width / cols
  cell_height = height / rows
  if cols > width or rows > height:
    raise ValueError('Too many cols or rows.')
  result = ""
  for i in range(rows):
    for j in range(cols):
      gray = np.mean(
        frame[int(i * cell_height):min(int((i + 1) * cell_height), height), int(j * cell_width):min(int((j + 1) * cell_width), width)]
      )
      result += grayToChar(gray)
    result += '\n'
  return result

def grayToChar(gray):
  CHAR_LIST = ' .:-=+*#%@'
  num_chars = len(CHAR_LIST)
  return CHAR_LIST[
    min(
      int(gray * num_chars / 255),
      num_chars - 1
    )
  ]
  
if __name__ == '__main__':
    main()

"""

"""
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\username_text_file.txt", "r") as f: #create a text file with the usernames you want to check
  data = f.readlines()

for un in data:
    time.sleep(1 * random.random())
    url = "https://www.instagram.com/"+str(un[:4])
    x = requests.get(url, verify = False)
    if x.status_code == 200:
        print("skip - " + un[:4]+ " - "+ str(data.index(un)))
    else:
        print("available - " + un[:4] + " - "+ str(data.index(un)))
        with open("available_usernames.txt", "a") as f2: # create a blank text file and it'll insert all the available usernames in there so you can check later
          f2.write(un)
    if int(data.index(un))%20 == 0:
        time.sleep(5)
"""

