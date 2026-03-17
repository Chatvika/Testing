import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
# By ID
driver.find_element(By.CSS_SELECTOR, "#username")

# By Class
driver.find_element(By.CSS_SELECTOR, ".login-btn")

# By Attribute
driver.find_element(By.CSS_SELECTOR, "input[type='email']")

# Combination
driver.find_element(By.CSS_SELECTOR, "input.form-control[type='text']")

# Contains
driver.find_element(By.XPATH, "//input[contains(@id,'user')]")

# Starts-with
driver.find_element(By.XPATH, "//input[starts-with(@id,'user')]")

# Text
driver.find_element(By.XPATH, "//button[text()='Login']")

# Multiple attributes
driver.find_element(By.XPATH, "//input[@type='text' and @name='username']")