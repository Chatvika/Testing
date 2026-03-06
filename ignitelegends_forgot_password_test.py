"""IgniteLegends Forgot Password Tests using Selenium"""
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


def navigate_to_forgot_password(driver):
    """Navigate to forgot password page"""
    driver.get("https://dev.ignitelegends.com/")
    time.sleep(3)
    # Click login button first
    try:
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))
        )
        login_button.click()
        time.sleep(2)
    except:
        pass
    # Find and click forgot password link
    forgot_password_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Forgot') and contains(text(),'Password')]"))
    )
    forgot_password_link.click()
    time.sleep(2)


def submit_forgot_password(driver, email):
    """Submit forgot password form with given email"""
    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email' or contains(@placeholder,'Email')]"))
    )
    email_field.clear()
    email_field.send_keys(email)
    
    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()
    time.sleep(3)


def test_forgot_password_valid_email():
    """Test Case 1: Valid email - should show success message"""
    print("\n" + "="*50)
    print("TEST 1: Forgot Password with Valid Email")
    print("="*50)
    
    driver = setup_driver()
    try:
        navigate_to_forgot_password(driver)
        submit_forgot_password(driver, "naganaboyinachatvika@gmail.com")
        print(f"Current URL: {driver.current_url}")
        # Check for success message or password reset email sent
        page_source = driver.page_source.lower()
        success_indicators = ["sent", "success", "check your email", "reset link"]
        found_success = any(indicator in page_source for indicator in success_indicators)
        print(f"Success message found: {found_success}")
        print("TEST 1: Completed")
    except Exception as e:
        print(f"TEST 1 Error: {e}")
    finally:
        driver.quit()


def test_forgot_password_invalid_email():
    """Test Case 2: Invalid email - should show error message"""
    print("\n" + "="*50)
    print("TEST 2: Forgot Password with Invalid Email")
    print("="*50)
    
    driver = setup_driver()
    try:
        navigate_to_forgot_password(driver)
        submit_forgot_password(driver, "notregistered@test.com")
        print(f"Current URL: {driver.current_url}")
        page_source = driver.page_source.lower()
        error_indicators = ["not found", "invalid", "error", "does not exist"]
        found_error = any(indicator in page_source for indicator in error_indicators)
        print(f"Error message found: {found_error}")
        print("TEST 2: Completed")
    except Exception as e:
        print(f"TEST 2 Error: {e}")
    finally:
        driver.quit()


def test_forgot_password_empty_email():
    """Test Case 3: Empty email - should show validation error"""
    print("\n" + "="*50)
    print("TEST 3: Forgot Password with Empty Email")
    print("="*50)
    
    driver = setup_driver()
    try:
        navigate_to_forgot_password(driver)
        submit_forgot_password(driver, "")
        print(f"Current URL: {driver.current_url}")
        print("TEST 3: Completed - Check for validation error")
    except Exception as e:
        print(f"TEST 3 Error: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    print("="*50)
    print("IgniteLegends Forgot Password Tests")
    print("="*50)
    
    test_forgot_password_valid_email()
    test_forgot_password_invalid_email()
    test_forgot_password_empty_email()
    
    print("\n" + "="*50)
    print("All Forgot Password Tests Completed!")
    print("="*50)

