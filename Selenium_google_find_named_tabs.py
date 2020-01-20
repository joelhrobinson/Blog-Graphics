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

element = driver.find_elements_by_id('logo')                # source code   <div id="logo">
print ('found id=logo')
element = driver.find_elements_by_class_name('search-icon') # <div class="search-icon"></div>'
print ('found class=search-icon')
element = driver.find_elements_by_link_text('chrome-search://local-ntp/voice.css')
print ('found link text')
# href="chrome-search://local-ntp/voice.css"></link>
print ('Have the elements', element)
print ('done')

#for ii in ids:
    #print ii.tag_name
 #   print ids.get_attribute('id')    # id name as string

#find_elements_by_tag_name()
#find_elements_by_id()
#find_elements_by_css_selector()
#find_elements_by_xpath()