from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.nytimes.com/search?query=a&sort=newest")

items = driver.find_elements(By.CSS_SELECTOR, 'h4')

for i in items:
	print(i.text)

driver.set_window_size(1280,960)
time.sleep(2)

driver.save_screenshot("screenshot.png")
time.sleep(2)

driver.close()