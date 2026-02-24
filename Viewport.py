from selenium import webdriver
import time
viewports=[(1024,768),(768,1024),(375,667),(414,896)]

browser=webdriver.Chrome()
browser.get('https://www.google.com')

browser.set_window_size(width=768,height=1024)
time.sleep(3)

try :
    for width,height in viewports:
        browser.set_window_size(width,height)
        time.sleep(4)

finally:
    browser.close()