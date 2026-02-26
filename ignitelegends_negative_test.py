"""
IgniteLegends Negative Login Tests using Selenium
This script tests negative login scenarios on https://dev.ignitelegends.com/
"""
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def setup_driver():
    """Set up Edge driver"""
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--disable-extensions")
    return webdriver.Edge(options=edge_options)


def find_and_fill_login_form(driver, email, password):
    """Helper to find and fill login form"""
    # Find email field
    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email' or contains(@placeholder,'Email')]"))
    )
    email_field.clear()
    email_field.send_keys(email)
    
    # Find password field
    password_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.clear()
    password_field.send_keys(password)
    
    # Click submit
    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()
    time.sleep(2)


def navigate_to_login(driver):
    """Navigate to login page"""
    driver.get("https://dev.ignitelegends.com/")
    time.sleep(3)
    
    # Click login button
    try:
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))
        )
        login_button.click()
    except:
        pass
    time.sleep(2)


def test_invalid_email_format():
    """Test Case 1: Invalid email format"""
    print("\n" + "="*50)
    print("TEST 1: Invalid Email Format")
    print("="*50)
    
    driver = setup_driver()
    try:
        navigate_to_login(driver)
        find_and_fill_login_form(driver, "invalidemail", "Pavan123$")
        time.sleep(3)
        print(f"Current URL: {driver.current_url}")
        print("TEST 1: Completed - Check for error message")
    except Exception as e:
        print(f"TEST 1 Error: {e}")
    finally:
        time.sleep(2)
        driver.quit()


def test_invalid_password():
    """Test Case 2: Invalid password"""
    print("\n" + "="*50)
    print("TEST 2: Invalid Password")
    print("="*50)
    
    driver = setup_driver()
    try:
        navigate_to_login(driver)
        find_and_fill_login_form(driver, "pavanchenu15@gmail.com", "WrongPassword")
        time.sleep(3)
        print(f"Current URL: {driver.current_url}")
        print("TEST 2: Completed - Check for error message")
    except Exception as e:
        print(f"TEST 2 Error: {e}")
    finally:
        time.sleep(2)
        driver.quit()


def test_empty_credentials():
    """Test Case 3: Empty credentials"""
    print("\n" + "="*50)
    print("TEST 3: Empty Credentials")
    print("="*50)
    
    driver = setup_driver()
    try:
        navigate_to_login(driver)
        find_and_fill_login_form(driver, "", "")
        time.sleep(3)
        print(f"Current URL: {driver.current_url}")
        print("TEST 3: Completed - Check for validation errors")
    except Exception as e:
        print(f"TEST 3 Error: {e}")
    finally:
        time.sleep(2)
        driver.quit()


def test_wrong_credentials():
    """Test Case 4: Wrong credentials"""
    print("\n" + "="*50)
    print("TEST 4: Wrong Credentials")
    print("="*50)
    
    driver = setup_driver()
    try:
        navigate_to_login(driver)
        find_and_fill_login_form(driver, "wrong@test.com", "WrongPass123")
        time.sleep(3)
        print(f"Current URL: {driver.current_url}")
        print("TEST 4: Completed - Check for error message")
    except Exception as e:
        print(f"TEST 4 Error: {e}")
    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    print("="*50)
    print("IgniteLegends Negative Login Tests")
    print("="*50)
    
    test_invalid_email_format()
    test_invalid_password()
    test_empty_credentials()
    test_wrong_credentials()
    
    print("\n" + "="*50)
    print("All Negative Tests Completed!")
    print("="*50)
