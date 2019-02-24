#!/usr/bin/python
import requests
from bs4 import BeautifulSoup as bs

def main():
  city, state = get_city_and_state()
  html = get_weather_html(city, state)
  parse_html_for_weather(html)
  # display forecast

def get_city_and_state():
  city = input("enter city for the weather report: ")
  state = input("enter two character abbreviation for state: ")
  return city, state

def get_weather_html(city, state):
  url = "https://www.wunderground.com/weather/us/{}/{}".format(state, city)
  res = requests.get(url)
  if res.status_code == 200:
    html = bs(res.text, "html.parser")
    return html  
  else:
    print("Error getting web data. Response {}, {}".format(res.status_code, res.text))
    sys.exit(-1)
 
def parse_html_for_weather(html):
  # Stationname: $('div.station-nav a.station-name').text
  # Temp: $('div.current-temp span.wu-value').textContent
  # scale: $('div.current-temp span.wu-label').textContent
  # conditions: $('.conditions-extra p').textContent 
  station = html.find(class_='station-nav').find(class_='station-name').text.strip().split('\n')[-1].strip()
  temp = html.find(class_='current-temp').find(class_='wu-value').text.strip()
  scale = html.find(class_='current-temp').find(class_='wu-label').text.strip()
  conditions = html.find(class_='conditions-extra').find('p').text.strip()
  print(station, conditions, temp, scale)


if __name__ == '__main__':
  main()
