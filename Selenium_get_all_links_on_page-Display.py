############# tag_name ###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
#############################
element = 'Sorry!!!'
driver.get('http://google.com')


hreflinks = driver.find_elements_by_xpath("//a[@href]")



######## PRINT a while loop ##########################
while len(hreflinks):
    linkurl = hreflinks.pop()
    linkurl = linkurl.get_attribute("href")

    print(linkurl)
    print ("Joel: Loop 2 Done")
######## PRINT a for loop ##########################
for elem in hreflinks:
    print(elem.get_attribute("href"))
print ("Joel: Loop 3 Done")
