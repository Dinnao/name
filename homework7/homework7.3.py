import requests
from datetime import datetime

API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'

def weather_forecast():
    city_name = input('Please enter your city:\n')
    cnt = int(input('Please enter the quantity of days:\n'))
    data = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?',
                        params={'q': city_name, 'cnt': cnt, 'appid': API_KEY}).json()
    file_name = datetime.now().strftime('%d-%m-%Y') \
                + '-' + str(city_name) + '-' \
                + str(cnt) + '-days-weather-forecast.txt'
    with open(file_name, 'w') as file:
        file.write('Date:\t\t Day:\t Night:\t Feels like(day):\t Feels like(night):\n')
        for data_list in data['list']:
            file.write(str(datetime.fromtimestamp(data_list['dt']))) #не хочет форматировать с инта в стрфтайм. почему?
            file.write(str(data_list['temp']['day']) + '\t')
            file.write(str(data_list['temp']['night']) + '\t\t')
            file.write(str(data_list['feels_like']['day']) + '\t\t\t\t')
            file.write(str(data_list['feels_like']['night']) + '\n')
        file.close()
weather_forecast()



