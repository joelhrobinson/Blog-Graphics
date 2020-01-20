############################################
## JOEL: you need to set up the path variable first.  It cannot find the files 
# copy chromedriver.exe to d:\bin, then change system variable to include c:\bin
# the end
#############################################
import time
from selenium import webdriver
driver = webdriver.Chrome()

# open the the google web page
driver.get ('http://google.com')

time.sleep (5)
print ('Have the elements')
print (elements)
print ('done')

#for ii in ids:
    #print ii.tag_name
 #   print ids.get_attribute('id')    # id name as string

#find_elements_by_tag_name()
#find_elements_by_id()
#find_elements_by_css_selector()
#find_elements_by_xpath()