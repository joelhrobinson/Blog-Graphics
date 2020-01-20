from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username="joelhrobinson"
userpw  ="Retire2019FB"

# open the the web page
driver = webdriver.Chrome()
driver.get ('http://www.facebook.com')

element = driver.find_element_by_id("email")
print ("Opened facebook, now logging using Chrome")
element.send_keys(username)
element = driver.find_element_by_id("pass")
element.send_keys(userpw)
element.send_keys(Keys.RETURN)
print ("logged in")




# simulate someone pressing the RETURN or enter key
#       element = driver.find_element_by_name('q'  )
#       element.send_keys('test')
#       from selenium.webdriver.common.keys import Keys
#       element.send_keys(Keys.RETURN)
# the end
