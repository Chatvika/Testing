"""
IgniteLegends Login Test using Selenium
This script tests the login functionality on https://dev.ignitelegends.com/
Using Microsoft Edge browser
"""
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time


def test_ignitelegends_login():
    """
    Test case: Login to IgniteLegends application
    Credentials: pavanchenu15@gmail.com / Pavan123$
    """
    # Set up Edge options
    edge_options = Options()
    edge_options.add_argument("--start-maximized")  # Maximize the browser window
    edge_options.add_argument("--disable-extensions")  # Disable extensions for faster loading
    
    # Set up the Edge driver (using Edge's built-in driver)
    driver = webdriver.Edge(options=edge_options)
    
    try:
        # Navigate to the application
        print("Navigating to https://dev.ignitelegends.com/...")
        driver.get("https://dev.ignitelegends.com/")
        
        # Wait for the page to load
        time.sleep(3)
        
        # Print page title for verification
        print(f"Page title: {driver.title}")
        
        # Wait for the login button to be visible and click it
        print("Looking for login button...")
        
        # Try to find and click the login button/link
        # Common selectors for login buttons
        login_selectors = [
            "//a[contains(text(),'Login')]",
            "//button[contains(text(),'Login')]",
            "//a[contains(@href,'login')]",
            "//button[contains(@class,'login')]",
            "//a[contains(@class,'login')]",
            "//div[contains(text(),'Login')]",
        ]
        
        login_button = None
        for selector in login_selectors:
            try:
                login_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                print(f"Found login button with selector: {selector}")
                break
            except:
                continue
        
        if login_button:
            login_button.click()
            print("Clicked login button")
            time.sleep(2)  # Wait for login form to appear
        else:
            print("Login button not found directly, looking for login form...")
        
        # Wait for the login form to load
        print("Waiting for login form...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        
        # Find email/username input field
        email_selectors = [
            "//input[@type='email']",
            "//input[contains(@placeholder,'Email')]",
            "//input[contains(@name,'email')]",
            "//input[contains(@id,'email')]",
            "//input[@type='text']",
        ]
        
        email_field = None
        for selector in email_selectors:
            try:
                email_field = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, selector))
                )
                print(f"Found email field with selector: {selector}")
                break
            except:
                continue
        
        if email_field:
            # Clear and enter email
            email_field.clear()
            email_field.send_keys("pavanchenu15@gmail.com")
            print("Entered email: pavanchenu15@gmail.com")
        
        # Find password input field
        password_selectors = [
            "//input[@type='password']",
            "//input[contains(@placeholder,'Password')]",
            "//input[contains(@name,'password')]",
            "//input[contains(@id,'password')]",
        ]
        
        password_field = None
        for selector in password_selectors:
            try:
                password_field = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, selector))
                )
                print(f"Found password field with selector: {selector}")
                break
            except:
                continue
        
        if password_field:
            # Clear and enter password
            password_field.clear()
            password_field.send_keys("Pavan123$")
            print("Entered password: Pavan123$")
        
        # Find and click the submit/login button
        submit_selectors = [
            "//button[@type='submit']",
            "//button[contains(text(),'Login')]",
            "//button[contains(text(),'Sign In')]",
            "//input[@type='submit']",
            "//a[contains(text(),'Login')]",
        ]
        
        submit_button = None
        for selector in submit_selectors:
            try:
                submit_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                print(f"Found submit button with selector: {selector}")
                break
            except:
                continue
        
        if submit_button:
            submit_button.click()
            print("Clicked login/submit button")
            time.sleep(3)  # Wait for login to process
            
            # Check if login was successful (you can add verification here)
            print(f"Current URL after login attempt: {driver.current_url}")
            print(f"Page title after login: {driver.title}")
            
            print("✅ Login test completed successfully!")
        else:
            print("❌ Submit button not found")
            
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Keep browser open for 5 seconds to see the result
        time.sleep(5)
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    print("=" * 60)
    print("IgniteLegends Login Test - Edge Browser")
    print("=" * 60)
    test_ignitelegends_login() 
    print("=" * 60)
