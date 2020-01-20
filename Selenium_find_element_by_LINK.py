############################################
# WORKS About   Store    Gmail   Business,   Advertising,   Images
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
#############################
driver.get("https://www.google.com/")
print ("Enter link name to search google.com CASE SENSITIVE!!!!: ")
mystring = input()  
element = 'SORRY!!!'
print ("Searching google for element link named: ", mystring)

try:
    element = driver.find_element_by_link_text(mystring)
    print (mystring, " link found \n ", element)
except:
    print (mystring, " link NOT found \n ", element)
#############################
try:
    element = driver.find_element_by_partial_link_text(mystring) 
    print (mystring, " partial link found \n ", element)
except:
    print (mystring, "partial link NOT found \n ", element)
print ("Joel: Done")



