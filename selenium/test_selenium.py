
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
import time
import selenium as sel
from selenium import webdriver # need to do it this way

# access to the keyboard keys
from selenium.webdriver.common.keys import Keys
k = sel.webdriver.common.keys.Keys # or this


# explicit waits (selenium)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# this is where the chrome driver exe sits
PATH = "C:\Program Files (x86)\chromedriver.exe"


# versions
print('the selenium package is:', sel.__package__)
print('the selenium version is:', sel.__version__)

# set driver to selenium webdriver
driver = webdriver.Chrome(PATH)

# get a url
url = 'http://www.lemsolutions.co.uk/'
url = 'https://techwithtim.net'
driver.get(url)
print(driver.title)

# seems to quit before this anyway
# driver.quit()


print('now do the functions procedure')


'''
access elements of webpage using certain properties:
id, class, name, tag
most common (in order or uniqueness):
[1] id, [2] name, [3] class


'''
# identify search box (from site)
search = driver.find_element_by_name('s')
search.send_keys('test') #type "test"
search.send_keys(Keys.RETURN) # hit Enter

# print(driver.page_source) # the source code

# need to pause
# time.sleep(5)

# need explicit waits selenium to wait for page result
# https://selenium-python.readthedocs.io/waits.html


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)

    # find all elements in a specific tag
    articles = main.find_elements_by_tag_name('article')

    # loop throught articles getting entry summary
    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)


finally:
    driver.quit()


# main = driver.find_elements_by_id('main')

