from selenium import webdriver
from selenium . webdriver. common.by import By
url = "https://jqueryui.com/"

driver =webdriver.Chrome()
driver.maximize_window()
driver.get(url)

all_links = driver.find_elements(By.TAG_NAME,value='a')
print(f"Total numer of liks on the page: {len(all_links)}")
