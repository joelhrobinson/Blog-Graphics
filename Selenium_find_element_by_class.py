############################################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
#############################
# FAILS DUE TO SPACES  <div id="page" class="hfeed site">
# WORKS <article id="post-2" class="post-2 page type-page status-publish hentry">
# WORKS <div id="content" class="site-content">
# WORKS	<div class="row">
# WORKS	<div class="c6"></div>
element = 'Sorry!!!'
print ("Enter CLASS name to search joelhrobinson.com CASE SENSITIVE!!!!: ")
mystring = (input() ) 
print ("Searching google for element CLASS named: ", mystring)

driver.get("http://www.joelhrobinson.com/")
try:
    element = driver.find_element_by_class_name(mystring)
    print (mystring, "www.joelhrobinson.com CLASS WAS found \n ", element)
except:
    print (mystring, "www.joelhrobinson.com CLASS NOT found \n ", element)
#############################

print ("Joel: Done")



