############# tag_name ###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
#############################
# getElementsByTagName("head")
element = 'Sorry!!!'
print ("Enter tag_name name to search joelhrobinson.com CASE SENSITIVE!!!!: ")
mystring = (input() ) 
print ("Searching www.joelhrobinson.com for element tag_name: ", mystring)

driver.get("http://www.joelhrobinson.com/  FAILS")
try:
    element = driver.find_element_by_class_tag_name(mystring)
    print (mystring, "www.joelhrobinson.com tag_name WAS found \n ", element)
except:
    print (mystring, "www.joelhrobinson.com tag_name NOT found \n ", element)
#############################

print ("Joel: Done")



