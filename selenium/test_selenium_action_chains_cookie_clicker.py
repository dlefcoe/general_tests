'''
downloads:
Chrome Web-driver Download: https://sites.google.com/a/chromium.org/chromedriver/downloads
Selenium Documentation: https://selenium-python.readthedocs.io/
selenium action chains: https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains


'''

# imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# imports for explicit waits (selenium)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import action chains
from selenium.webdriver.common.action_chains import ActionChains

# keep browser open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# the webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=PATH)

# get the url DOM
url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)

# implicit wait
driver.implicitly_wait(5)


cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')

# items = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5_000_000):
    actions.perform()
    print('the click has been performed:' + str(i))
    # count = int( cookie_count.text.split(' ')[0] )
    # for item in items:
    #     value = int(item.text)
    #     if value <= count:
    #         upgrade_actions = ActionChains(driver)
    #         upgrade_actions.move_to_element(item)
    #         upgrade_actions.click()
    #         upgrade_actions.perform()
    

print('all done')





# # find link and click it
# link = driver.find_element_by_link_text('Python Programming')
# link.click()


# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()

#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     element.clear() #clear before click
#     element.click()

#     # back 3 pages
#     driver.back()
#     driver.back()
#     driver.back()

#     # forward 2 pages
#     driver.forward()
#     driver.forward()

#     print('waiting for 3 seconds...')
#     time.sleep(3)

# except:
#     driver.quit()








