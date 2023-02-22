from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.nytimes.com/search?query=+")

items = driver.find_elements(By.CSS_SELECTOR, 'h4')

for i in items:
	print(i.text)

driver.close()