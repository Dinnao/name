#w = input('Enter some string: ')
#def fstr_tolst(w):
#   print(w)
#@fstr_tolst(w) #Вообще не шарю как работают декораторы
#def word():
#    some = w.split(' ')
#    print(some)
#word()


#steps = []
#def step(Cel):
#    while Cel != 0:
#        steps.append(1)
#        Cel -= 1
#step(int(input('Please enter Celsius: ')))
#def calculate_far(Cel):
#    Cel = len(steps)
#    Far = Cel * 1.8 + 32
#    print('In fahrenheit: ' + str(Far))
#def calculate_kel(Cel):
#    Cel = len(steps)
#    Kel = Cel + 273.15
#    print('In kelvins: ' + str(Kel))
#calculate_far(1)
#calculate_kel(1)


#import requests
#from datetime import datetime
#
#API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'
#
#def weather_forecast():
#    city_name = input('Please enter your city:\n')
#    cnt = int(input('Please enter the quantity of days:\n'))
#    data = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?',
#                        params={'q': city_name, 'cnt': cnt, 'appid': API_KEY}).json()
#    file_name = datetime.now().strftime('%d-%m-%Y') \
#                + '-' + str(city_name) + '-' \
#                + str(cnt) + '-days-weather-forecast.txt'
#    with open(file_name, 'w') as file:
#        file.write('Dante:\t\t Day:\t Night:\t Feels like(day):\t Feels like(night):\n')
#        for data_list in data['list']:
#            file.write(str(datetime.fromtimestamp(data_list['dt'].strftime('%d-%m-%Y') + '\t'))) #не хочет форматировать с инта в стрфтайм. почему?
#            file.write(str(data_list['temp']['day'] + '\t'))
#            file.write(str(float(data_list['temp']['night'])) + '\t\t')
#            file.write(str(data_list['feels like']['day']) + '\t\t\t\t')
#            file.write(str(data_list['feels like']['night']) + '\n')
#        file.close()
#weather_forecast()



