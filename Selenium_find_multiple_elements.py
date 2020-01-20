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
    #print ii.tag_name
    print (ii.get_attribute('id')  )  # id name as string
print ("Joel: Done")



