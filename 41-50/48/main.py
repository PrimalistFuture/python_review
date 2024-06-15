from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome brower open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dates = driver.find_elements(
    By.XPATH, value="""//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time""")
days = [date.text for date in dates]
# print(days)

events = driver.find_elements(
    By.XPATH, value="""//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a""")
names = [event.text for event in events]
# print(names)

upcoming_events = {}
for n in range(len(names)):
    upcoming_events[n] = {
        "time": days[n],
        "name": names[n]
    }

print(upcoming_events)
driver.quit()
