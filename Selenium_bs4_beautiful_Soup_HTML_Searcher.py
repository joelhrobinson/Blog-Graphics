############# tag_name ###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
######### HTML DOM   #####################
from htmldom import htmldom
######### import urllib #########################
import urllib
from urllib.request import urlopen

######### import BS4 #########################
import bs4
from bs4 import BeautifulSoup

######### get data #########################
data=requests.request('get','https://google.com/') #any website
s=bs4.BeautifulSoup(data.text,'html.parser')
for link in s.findAll('a'):
    print(link)
print ("Joel: Loop 1 Done------------------------------------")

######## PRINT a while loop ##########################
while len(hreflinks1):
    linkurl = hreflinks1.pop()
    linkurl = linkurl.get_attribute("href")

    print(linkurl)
print ("Joel: Loop 2 Done------------------------------------")
