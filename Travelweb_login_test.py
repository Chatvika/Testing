from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Browser setup
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Edge(options=options)

# Open website
driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver,10)

# Enter username
username = wait.until(
    EC.presence_of_element_located((By.ID,"user-name"))
)
username.send_keys("standard_user")

# Enter password
password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")

# Click login
driver.find_element(By.ID,"login-button").click()

# Verify login success
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME,"inventory_list"))
)

print("Login Test Passed")

time.sleep(3)

# Close browser
driver.quit()