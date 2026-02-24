from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Edge()

browser.get(' https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
browser.maximize_window()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight):")

checkboxes=browser.find_elements(By.XPATH,value="//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count =0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count+=1

expected_checked_count = 9

if checked_count==expected_checked_count:
    print('checkbox count verified')
else:
    print('checkbox count mismathed ')
time.sleep(5)
browser.close()