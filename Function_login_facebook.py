# simple function log into
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
############################################################
# DEFINE FUNCTION BEFORE USING IT
def loginFB():     
    username="joelhrobinson"
    userpw  ="Retire2019FB"

    # open the the web page
    driver = webdriver.Chrome()
    driver.get ('http://www.facebook.com')

    element = driver.find_element_by_id("email")
    print ("loginFB: Opened facebook, now logging using Chrome")
    element.send_keys(username)
    element = driver.find_element_by_id("pass")
    element.send_keys(userpw)
    element.send_keys(Keys.RETURN)
    print ("loginFB: logged in")
# ----------------------------------------------------------------
#print ("loginFB: Invoking loginfacebook function")
#loginFB()   
#print ("loginFB: Return from loginfacebook function")