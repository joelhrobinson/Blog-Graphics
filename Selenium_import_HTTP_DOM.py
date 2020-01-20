

# pip install htmldom

# You can import the HTML dom using html dom library in python. You can find it over here and install it using PIP:
# https://pypi.python.org/pypi/htmldom/2.0
# htmldom-2.0.win-amd64.exe (235.3 kB) 
#
from htmldom import htmldom
dom = htmldom.HtmlDom("https://www.github.com/")  
dom = dom.createDom()
print ('HTML DOM 2.0 Installed')