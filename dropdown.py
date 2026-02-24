from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Edge()
driver.maximize_window()
login_url="https://the-internet.hackerearth.com//dropdown "
driver.get(login_url)

dropdown_element =driver.find_element(By.ID,value="dropdown")
target_value = "Option 3"
select =Select(dropdown_element)
for option in select. options:
    if option.text == target_value:
        option.click()
        print(f"Selected Option is {target_value}")
        break 
    else:
        print(f"Option '{target_value}' not found")


