############################################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
#############################
#   <div id="page" class="hfeed site">
#   <article id="post-2" class="post-2 page type-page status-publish hentry">
# 	<div id="content" class="site-content">
#		<div class="row">
#			<div class="c6"></div>
element = 'Sorry!!!'
driver.get('http://www.joelhrobinson.com')

element = driver.find_elements_by_xpath('//*[@id]')

for ii in element:
    # id name as string 
    print ("www.joelhrobinson.com Found tag_name and id: ",ii.tag_name, ii.get_attribute('id')  ) 
print ("Joel: Done")