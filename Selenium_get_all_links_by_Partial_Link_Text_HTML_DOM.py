############# tag_name ###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
######## HTML DOM #####################
from htmldom import htmldom
##################################

driver.get('http://joelhrobinson.com')
hreflinks1 = driver.find_elements_by_partial_link_text('')
hreflinks2 = driver.find_elements_by_xpath("//a[@href]")


######## PRINT a while loop ##########################
while len(hreflinks1):
    linkurl = hreflinks1.pop()
    linkurl = linkurl.get_attribute("href")

    print(linkurl)
print ("Joel: Loop 2 Done------------------------------------")
######## PRINT a for loop ##########################
for elem in hreflinks2:
    print(elem.get_attribute("href"))
print ("Joel: Loop 3 Done------compare lists")
