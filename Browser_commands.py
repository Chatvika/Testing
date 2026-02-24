''' 4). Browser commands selenium webdriver'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser =webdriver.Edge()
browser.get('https://opensource-demo.orangehrmlive.com/')
browser.fullscreen_window()
time.sleep(5)
browser.find_element(By.CSS_SELECTOR,value= ".oxd-text oxd-text--p orangehrm-login-forgot-header " )
browser.back()
time.sleep(5)
browser.forward()
time.sleep(5)
browser.refresh()
browser.close()