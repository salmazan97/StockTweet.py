import requests
import json
from datetime import date
from datetime import timedelta
#get yesterdays date and time
#yyyy-mm-dd
input_date = input('input date (yyyy-mm-dd): ')
input_ticker = input('input ticker name: ')
#replace date in link with yesterdays date
stockwatch_token = 'TOKEN'
stockwatch_url = 'https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey=11cJMechlND2APSxD6typ5g2ppXbKZup'.format(ticker= input_ticker,date = input_date)

#grab json dictionary and print to screen
response = requests.get(stockwatch_url)
r = response.json()
print('date: '+r['from'])
print('ticker: '+r['symbol'])
print('opened at: ' + str(r['open']))
print('closed at: '+ str(r['close']))