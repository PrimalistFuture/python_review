from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep Chrome brower open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# gets rid of errors and warnings
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first = driver.find_element(By.NAME, value="fName")
first.send_keys("Hello")

last = driver.find_element(By.NAME, value="lName")
last.send_keys("World")

email = driver.find_element(By.NAME, value="email")
email.send_keys("hello@world.com")

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()

driver.quit()
