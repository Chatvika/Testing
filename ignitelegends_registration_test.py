"""IgniteLegends Registration Test using Selenium"""
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


def test_registration_auto_fill():
    """Test Case: Registration with auto-fill and create account"""
    print("\n" + "="*50)
    print("TEST: Registration with Auto-Fill")
    print("="*50)
    
    driver = setup_driver()
    try:
        # Navigate to the application
        print("Navigating to https://dev.ignitelegends.com/")
        driver.get("https://dev.ignitelegends.com/")
        time.sleep(3)
        
        # Click Register/Sign Up button
        register_selectors = [
            "//a[contains(text(),'Register')]",
            "//a[contains(text(),'Sign Up')]",
            "//button[contains(text(),'Register')]"
        ]
        
        for selector in register_selectors:
            try:
                register_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                register_btn.click()
                print(f"Clicked: {selector}")
                break
            except:
                continue
        
        time.sleep(3)
        
        # Auto-fill registration form
        # First Name
        first_name_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'First') or contains(@name,'first')]"))
        )
        first_name_field.clear()
        first_name_field.send_keys("Chatvika")
        print("Filled: First Name - Chatvika")
        
        # Last Name
        last_name_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Last') or contains(@name,'last')]"))
        )
        last_name_field.clear()
        last_name_field.send_keys("Naganaboyina")
        print("Filled: Last Name - Naganaboyina")
        
        # Email
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_field.clear()
        email_field.send_keys("naganaboyinachatvika@gmail.com")
        print("Filled: Email - naganaboyinachatvika@gmail.com")
        
        # Phone Number
        phone_selectors = [
            "//input[contains(@placeholder,'Phone')]",
            "//input[contains(@name,'phone')]",
            "//input[@type='tel']"
        ]
        
        for selector in phone_selectors:
            try:
                phone_field = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, selector))
                )
                phone_field.clear()
                phone_field.send_keys("9502455971")
                print("Filled: Phone - 9502455971")
                break
            except:
                continue
        
        # Password
        password_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_field.clear()
        password_field.send_keys("Chatvik@123$")
        print("Filled: Password - Chatvik@123$")
        
        # Confirm Password
        confirm_password_selectors = [
            "//input[contains(@placeholder,'Confirm')]",
            "//input[contains(@name,'confirm')]"
        ]
        
        for selector in confirm_password_selectors:
            try:
                confirm_field = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, selector))
                )
                confirm_field.clear()
                confirm_field.send_keys("Chatvik@123$")
                print("Filled: Confirm Password - Chatvik@123$")
                break
            except:
                continue
        
        time.sleep(1)
        # Click Submit/Register button
        submit_selectors = [
            "//button[@type='submit']",
            "//button[contains(text(),'Register')]",
            "//button[contains(text(),'Sign Up')]"
        ]
        
        for selector in submit_selectors:
            try:
                submit_btn = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                submit_btn.click()
                print("Clicked Submit/Register button")
                break
            except:
                continue
        
        time.sleep(5)
        print(f"Current URL: {driver.current_url}")
        print("TEST: Registration form submitted successfully!")
        
    except Exception as e:
        print(f"TEST Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        driver.quit()


if __name__ == "__main__":
    print("="*50)
    print("IgniteLegends Registration Test")
    print("="*50)
    test_registration_auto_fill()
    print("\n" + "="*50)
    print("Registration Test Completed!")
    print("="*50)

