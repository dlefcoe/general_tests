'''
downloads:
Chrome Web-driver Download: https://sites.google.com/a/chromium.org/chromedriver/downloads
Selenium Documentation: https://selenium-python.readthedocs.io/
'''

# imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# imports for explicit waits (selenium)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# the webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# get the url DOM
url = 'https://techwithtim.net/'
driver.get(url)


# find link and click it
link = driver.find_element_by_link_text('Python Programming')
link.click()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.clear() #clear before click
    element.click()

    # back 3 pages
    driver.back()
    driver.back()
    driver.back()

    # forward 2 pages
    driver.forward()
    driver.forward()

    print('waiting for 3 seconds...')
    time.sleep(3)

except:
    driver.quit()




