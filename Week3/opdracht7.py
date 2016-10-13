import json, requests, sys
from pprint import pprint

# get command line arguments
if len(sys.argv) < 2:
    print('Usage: quick_weather.py location')
    sys.exit()

# argument 0 is program name
location = ' '.join(sys.argv[1:])

# download JSON data
# url = 'http://api.openweathermap.org/....?
response = requests.get('http://api.openweathermap.org/data/2.5/forecast/London?id=524901&APPID=59dd5641a0211d3f0a01fb2f23bcd09d')
response.raise_for_status()

# load JSON data into Python variable
weatherData = json.loads(response.text)

w = weatherData['list']
#pprint(w)

print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
