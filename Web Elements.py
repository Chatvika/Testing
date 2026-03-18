from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# # setup driver
driver=webdriver.Edge()
driver.maximize_window()

# # open demo site
driver.get ("https://demoqa.com/automation-practice-form")

time.sleep(2)

# # css selector
first_name=driver.find_element(By.CSS_SELECTOR,"#firstName")
first_name.send_keys("Chatvika")

# # dynamic xpath ex
last_name=driver.find_elements(By.XPATH,"//input[contains(@placeholder,'Last')]")
last_name.send_keys("N")

# # Radio Button
gender=driver.find_element(By.XPATH,"//label[text()='Female']")
gender.click()

time.sleep(2)

# check box
hobbies=driver.find_element(By.XPATH,"//label[text()='Sports']")
hobbies.click()

time.sleep(2)

# drop down
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(By.ID, "dropdown"))

dropdown.select_by_visible_text("Option 1")
time.sleep(1)

dropdown.select_by_index(2)
time.sleep(1)
#  File Upload
# -----------------------------------
driver.get("https://the-internet.herokuapp.com/upload")

file_input = driver.find_element(By.ID, "file-upload")

# Give file path from your system
file_input.send_keys("C:\\Users\\YourName\\Desktop\\testfile.txt")

upload_btn = driver.find_element(By.ID, "file-submit")
upload_btn.click()

time.sleep(3)

driver.quit()


