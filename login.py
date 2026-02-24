''' First Automation Script'''

from selenium import webdriver

browser =webdriver.Edge()
browser.get("https://dev.ignitelegends.com/")
browser.maximize_window()    #maximize the window
title=browser.title
print(title)
assert "Selenium" in title
