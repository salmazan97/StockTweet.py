import time
import random
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from datetime import timedelta

class Twitterbot():
    def __init__(self,username,password):
        self.browser = webdriver.Chrome('./chromedriver')
        self.username = username
        self.password = password

    
    def signIn(self):
        self.browser.implicitly_wait(50)
        self.browser.get('https://twitter.com/i/flow/login')
        usernameInput = self.browser.find_element(By.NAME, 'text')
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        passwordInput = self.browser.find_element(By.NAME, 'password')
        passwordInput.send_keys('Test1234!!')
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
    def get_gme:
        #get yesterdays date and time
        #yyyy-mm-dd
        today = date.today()
        yesterday_date = today - timedelta(days = 1)
        #replace date in link with yesterdays date
        stockwatch_token = 'TOKEN'
        stockwatch_url = 'https://api.polygon.io/v1/open-close/GME/{date}?adjusted=true&apiKey=11cJMechlND2APSxD6typ5g2ppXbKZup'.format(date = yesterday_date)
        #grab json dictionary and print to screen
        response = requests.get(stockwatch_url)
        r = response.json()
        response = requests.get(stockwatch_url)
        r = response.json()
        date = 'date: '+r['from']
        ticker = 'ticker: '+r['symbol']
        opened = 'opened at: ' + str(r['open'])
        closed = 'closed at: '+ str(r['close'])

    def TestTweet(self):
        funkyword = (date + ticker + opened + closed)
        self.browser.implicitly_wait(50)
        tweetpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        tweet = self.browser.find_element(By.XPATH, tweetpath)
        tweet.send_keys(funkyword)
        tweetbutton = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweetbutton.click()
    



		
if __name__ ==  '__main__' :
    username = '****'
    password = '****'
    t = Twitterbot(username,password)
    t.signIn()
    count = 0
    while count < 15:
        t.TestTweet()
        count += 1
