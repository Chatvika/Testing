'''syncronization : waiting for elements to load before interacting'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.maximize_window ()

driver.get("https://example.com/login")

# create wait object
wait =WebDriverWait(driver, 10)
# wait for username field
username =wait.until(EC.visiablity_of_element_located((By.ID, "username")))
username.send_keys("admin")
# wait for password field
password = wait.until(EC.visiablity_of_element_located((By.ID, "password")))
password.send_keys("1234")

# wait for login button and click
login_btn =wait.until(EC.visiablity_of_element_located((By.ID, "loginbtn")))
login_btn.click()

driver.quit()
