"""IgniteLegends Logout Test"""
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

# Configure Edge options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Edge(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})

driver.get("https://dev.ignitelegends.com/")
time.sleep(5)

# Login
driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("pavanchenu15@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Pavan123$")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(8)

# Click profile menu
for selector in ["//div[contains(@class,'profile')]", "//img[contains(@class,'avatar')]", "//span[contains(@class,'user')]"]:
    try:
        driver.find_element(By.XPATH, selector).click()
        break
    except:
        continue
time.sleep(2)

# Click logout
for selector in ["//a[contains(text(),'Logout')]", "//button[contains(text(),'Logout')]", "//span[contains(text(),'Logout')]"]:
    try:
        driver.find_element(By.XPATH, selector).click()
        print("Logged out successfully")
        break
    except:
        continue

time.sleep(3)
print(f"URL: {driver.current_url}")
driver.quit()

