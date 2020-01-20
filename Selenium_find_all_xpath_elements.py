############# tag_name ###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
#############################
element = 'Sorry!!!'
driver.get('http://google.com')

ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    # id name as string 
    x = ii.tag_name
    y = ii.get_attribute('id')
    z = ii.get_attribute('value')
    print ("tag_name id value: ",x,y ,z  ) 
print ("Joel: Done")
