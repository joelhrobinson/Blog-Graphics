############################################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
print ("Joel: searching https://www.google.com")
element = 'SORRY!!!'
# use find element
driver.get("https://www.google.com/")

##########################################################
# FIXED STRING
try:
    element = driver.find_element_by_link_text('About')
    print ("About link WAS found in https://www.google.com/\n ", element)
except:
    print ("About link NOT found in https://www.google.com/\n ", element)
#   element = driver.find_element_by_partial_link_text('About')t" 
# 
print ("Joel: Done")



