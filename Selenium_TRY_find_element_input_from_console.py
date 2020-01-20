############ NoSuchElementException ################################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

print ("Enter element name to search google.com for: ")
mystring = (input() ) 
element = 'SORRY!!!'
print ("Searching google for element named: ", mystring)
try:
    driver.get("https://www.google.com/")

    element = driver.find_element_by_name(mystring  )
    print ("Element ", mystring, " FOUND: \n ", element)

except:      
    print ("Element not found by name: ", mystring)
print ("Joel: Done")



