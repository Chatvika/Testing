from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_page_title(url, expected_title):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        driver.get(url)
        actual_title = driver.title
        
        if expected_title in actual_title:
            print("Test Passed ✅")
            return True
        else:
            print("Test Failed ❌")
            return False
    
    finally:
        driver.quit()


# Example Usage
test_page_title("https://www.google.com", "Google")
