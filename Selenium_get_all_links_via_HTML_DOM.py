############# tag_name ###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
####### IMPORT HTMLDOM ######################
from htmldom import htmldom


######## PRINT a while loop ##########################

print ("Joel: Calling DOM NOTE: page will not display")
dom = htmldom.HtmlDom("https://www.github.com/")  
dom = dom.createDom()
p_links = dom.find("a")  
for link in p_links:
  print ("URL: " +link.attr("href"))

print ("Joel: Done")
