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

    x = ii.tag_name
    h = ii.get_attribute('http')
    if h == 'None' or h == '':
        print ('found no http')
    y = ii.get_attribute('id')
    z = ii.get_attribute('value')
    print ("tag_name id value: ",x,y ,z,h  ) 
print ("Joel: Done")
