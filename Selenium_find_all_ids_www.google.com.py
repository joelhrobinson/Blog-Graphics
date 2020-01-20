############# tag_name ###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
#############################
element = 'Sorry!!!'
driver.get('http://google.com')

element = driver.find_elements_by_xpath('//*[@id]')

for ii in element:
    # id name as string 
    print ("www.google.com Found tag_name and id: ",ii.tag_name, ii.get_attribute('id')  ) 
print ("Joel: Done")



