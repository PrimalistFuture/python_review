from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Selenium Find Element Docs
# "https://selenium-python.readthedocs.io/locating-elements.html"


# Keep Chrome brower open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# gets rid of errors and warnings
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")

# Closes a sinlge tab
# driver.close()

# Closes the entire browser
# driver.quit()

# Using Selenium to move through Amazon
DUNE_URL = "https://www.amazon.com/dp/B0CF3MVMKH/"
driver.get(DUNE_URL)
# Getting around the captcha
captcha = driver.find_element(By.LINK_TEXT, "Try different image")
captcha.click()

# Finding the element by class
# Initially saved as an html element
price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# This is how we get the text
print(f"The price is ${price_whole.text}.{price_cents.text}")

# Would search for an element by NAME which you might see in a search bar
# Returns a selenium element
search_bar = driver.find_element(By.NAME, value="q")
# To get the text or other attributes
search_bar.tag_name()
search_bar.get_attribute("placeholder")

# Find by id
button = driver.find_element(By.ID, value="submit")

# Find element by CSS Selector
# finds a tag nested in a class of documentation-widget
link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(link.text)


# Find element by XPath
# XPATH locates element by path struture
# Can be copied from the dev tools thank god
price_with_xpath = driver.find_element(
    By.XPATH, value='''//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]''')
print(price_with_xpath.text)

# Find multiple elements
# all of the above could be done with elements, rather than element
driver.find_elements(By.CSS_SELECTOR, value=".documentation-widget a")

# Click on a link
# Can be done with any selector
captcha = driver.find_element(By.LINK_TEXT, "Try different image")
captcha.click()

# Typing into a search bar
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
# Hitting enter to search
search.send_keys(Keys.ENTER)

driver.quit()
