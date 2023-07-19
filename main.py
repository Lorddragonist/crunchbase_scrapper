import requests
from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time

def run():
    browser = uc.Chrome()    
    url = 'https://news.crunchbase.com/public/makeup-venture-unicorn-ipo-oddity/'
    browser.get(url)
    browser.implicitly_wait(10)

    html = browser.page_source
    soup = bs(html, 'lxml')

    title = soup.find('header',{'class':'entry-header'}).find('h1',{'class':'entry-title h1'}).text

    author = soup.find('span',{'class':'vcard author'}).find('a').text

    print('My title is:',title)
    print('My author is:',author)


if __name__ == "__main__":
    run()