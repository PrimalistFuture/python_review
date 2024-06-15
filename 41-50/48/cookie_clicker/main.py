from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome brower open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# gets rid of errors and warnings
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")


def find_and_click_most_expensive():
    """^^^"""
    store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    store_items.reverse()
    for item in store_items:
        if item.get_attribute("class") != "grayed":
            item.click()
            break


# sets timeout for 15 sec
timeout = time.time() + 15
while True:
    # pauses time
    time.sleep(0.1)
    cookie.click()
    if time.time() > timeout:
        find_and_click_most_expensive()
