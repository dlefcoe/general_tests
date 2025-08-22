
'''
chrome browser: yes
chrome web driver: need this

the chrome browser and web driver are 2 different things
need both for selenium to work


what version of chrome do we have ?
chrone > help >
Version 86.0.4240.75 (Official Build) (64-bit)


downloads:
Chrome Web-driver Download: https://sites.google.com/a/chromium.org/chromedriver/downloads
Selenium Documentation: https://selenium-python.readthedocs.io/


download zip file.
copy to windows folder: C:\Program Files (x86)


'''
import selenium as sel
from selenium import webdriver

# this is where the chrome driver exe sits
PATH = "C:\Program Files (x86)\chromedriver.exe"


# versions
print('the selenium package is:', sel.__package__)
print('the selenium version is:', sel.__version__)

# set driver to selenium webdriver
driver = webdriver.Chrome(PATH)

# get a url
driver.get('http://www.lemsolutions.co.uk/')
print(driver.title)

# seems to quit before this anyway
# driver.quit()




