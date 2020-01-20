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
element = driver.find_element_by_name('q'  )
print ('found name=q', element)
a = 'begin'
a = element.get_attribute("attribute name")
print ('attribute name', a)     # NONE type = "NoneType") cannot convert to string

element = driver.find_elements_by_id('logo')                # source code   <div id="logo">
print ('found id=logo', element)
element = driver.find_elements_by_class_name('search-icon') # <div class="search-icon"></div>'
print ('found class=search-icon', element)
element = driver.find_elements_by_link_text('chrome-search://local-ntp/voice.css')
print ('found link text', element)                          # href="chrome-search://local-ntp/voice.css"></link>
print ('done')





#find_elements_by_xpath()