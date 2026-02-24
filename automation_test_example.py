"""
Small Automation Testing Example using Selenium
This example demonstrates basic web automation testing with assertions
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_google_search():
    """
    Automation test: Open Google and verify the page loads correctly
    """
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com/")
        
        # Verify the page title
        assert "Google" in driver.title, f"Expected 'Google' in title, got: {driver.title}"
        print("✅ Page title verification passed!")
        
        # Wait for search box to be visible
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        
        # Enter search query
        search_box.send_keys("Automation Testing")
        
        # Submit the search
        search_box.submit()
        
        # Wait for results and verify
        WebDriverWait(driver, 10).until(
            EC.title_contains("Automation Testing")
        )
        
        print(f"✅ Search completed! Page title: {driver.title}")
        print("✅ Test PASSED!")
        
    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")
        raise
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        raise
        
    finally:
        # Clean up
        driver.quit()
        print("Browser closed.")


def test_w3schools_form():
    """
    Automation test: Fill out a form on W3Schools
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigate to W3Schools form page
        driver.get("https://www.w3schools.com/html/html_form_input_types.asp")
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        
        # Find and fill the firstname field
        firstname = driver.find_element(By.NAME, "fname")
        firstname.clear()
        firstname.send_keys("John")
        
        # Find and fill the lastname field  
        lastname = driver.find_element(By.NAME, "lname")
        lastname.clear()
        lastname.send_keys("Doe")
        
        print("✅ Form filled successfully!")
        print("✅ Test PASSED!")
        
    except Exception as e:
        print(f"❌ Test FAILED: {e}")
        raise
        
    finally:
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    print("=" * 50)
    print("Running Automation Test 1: Google Search")
    print("=" * 50)
    test_google_search()
    
    print("\n" + "=" * 50)
    print("Running Automation Test 2: W3Schools Form")
    print("=" * 50)
    test_w3schools_form()
    
    print("\n All tests completed!")



'''   Elements :                         Locators:
        -Checkboxes                        -ID
        -links                             -Name
        -Textfields                      -classname
                                        -css selector
   INTERACTION:                          -Xpath
        -text field typing                -Link Text
         typing something                 -Partial link Text
         -checkbox-                       -tag name'''


''' 3) Automate login functionality selenium Webdriver:   '''

from selenium import webdriver
from selenium.webdriver.common.by import By

browser =webdriver.Edge()
browser.maximize_window()    

username="standard_user"
password="secret_sauce"
login_url="https://www.saucedemo.com/"
browser.get(login_url)

username_field=browser.find_element(By.ID ,value="user-name")
password_field=browser.find_element(By.ID ,value="password")

username_field.send_keys(username)
password_field.send_keys(password)


login_button=browser.find_element(By.ID,value= "login-button")
assert  not login_button.get_attributr("disabled")
login_button.click()

success_element =browser.find_element(By.CSS_SELECTOR,value="title")
assert success_element.text=="Products"


