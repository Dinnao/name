import requests
import datetime

URL = 'https://api.exchangerate.host/convert'

path = 'symbols.json'

def currency_input():
    currency_from = input(str('Enter the 3 letter abbreviation of nte currancy from: '))
    if currency_from == '':
        currency_from = 'USD'
    currency_to = input('Enter the 3 letter abbreviation of nte currancy to: ')
    if currency_to == '':
        currency_to = 'UAH'
    currancy_amount = input('Enter the amount: ')
    if currancy_amount == '':
        currancy_amount = 100.00
    curancy_date = input('Enter date: ')
    if curancy_date == '':
        curancy_date = datetime.datetime.now()
    data = {'from': currency_from, 'to': currency_to, 'amount': currancy_amount, 'date': curancy_date}
    r = requests.get(URL, data)
    print(r.json())
currency_input()

