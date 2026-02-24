"""
Simple Test Case Example using Selenium
This is a basic Selenium automation test demonstrating fundamental testing patterns
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_demoqa_registration():
    """
    Simple test case: Navigate to DemoQA registration page and verify elements exist
    """
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigate to DemoQA practice form
        driver.get("https://demoqa.com/automation-practice-form")
        
        # Wait for the form to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        
        # Verify the first name field exists
        first_name = driver.find_element(By.ID, "firstName")
        assert first_name.is_displayed(), "First name field should be visible"
        print("✅ First name field found!")
        
        # Fill in the form
        first_name.send_keys("John")
        
        last_name = driver.find_element(By.ID, "lastName")
        last_name.send_keys("Doe")
        
        email = driver.find_element(By.ID, "userEmail")
        email.send_keys("john.doe@example.com")
        
        print("✅ Form fields filled successfully!")
        print("✅ Test PASSED!")
        
    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")
        raise
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        raise
        
    finally:
        driver.quit()
        print("Browser closed.")


def test_w3schools_homepage():
    """
    Simple test case: Verify W3Schools homepage loads correctly
    """
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigate to W3Schools
        driver.get("https://www.w3schools.com/")
        
        # Verify page title contains "W3Schools"
        assert "W3Schools" in driver.title, f"Expected 'W3Schools' in title, got: {driver.title}"
        print("✅ Page title verified!")
        
        # Find the search box
        search_box = driver.find_element(By.ID, "search2")
        assert search_box.is_displayed(), "Search box should be visible"
        print("✅ Search box found!")
        
        print("✅ Test PASSED!")
        
    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")
        raise
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        raise
        
    finally:
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    print("=" * 50)
    print("Running Simple Test Case 1: DemoQA Registration")
    print("=" * 50)
    test_demoqa_registration()
    
    print("\n" + "=" * 50)
    print("Running Simple Test Case 2: W3Schools Homepage")
    print("=" * 50)
    test_w3schools_homepage()
    
    print("\n✅ All tests completed successfully!")
