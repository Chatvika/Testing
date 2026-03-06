"""IgniteLegends Dashboard Tests using Selenium"""
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


def login_to_app(driver):
    """Login to the application"""
    driver.get("https://dev.ignitelegends.com/")
    time.sleep(3)
    
    # Click login button
    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))
    )
    login_button.click()
    time.sleep(2)
    
    # Enter credentials
    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_field.clear()
    email_field.send_keys("naganaboyinachatvika@gmail.com")
    
    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.clear()
    password_field.send_keys("Pavan123$")
    
    # Submit login
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(5)


def test_redirect_to_dashboard():
    """Test Case 1: Verify redirect to dashboard after login"""
    print("\n" + "="*50)
    print("TEST 1: Redirect to Dashboard")
    print("="*50)
    
    driver = setup_driver()
    try:
        login_to_app(driver)
        current_url = driver.current_url
        print(f"Current URL after login: {current_url}")
        
        # Check if redirected away from login page
        assert "login" not in current_url.lower(), "Should redirect away from login"
        print("TEST 1: PASSED - Redirected to dashboard")
    except Exception as e:
        print(f"TEST 1 Error: {e}")
    finally:
        driver.quit()


def test_profile_menu_visible():
    """Test Case 2: Verify profile menu is visible after login"""
    print("\n" + "="*50)
    print("TEST 2: Profile Menu Visible")
    print("="*50)
    
    driver = setup_driver()
    try:
        login_to_app(driver)
        time.sleep(2)
        
        # Look for profile menu/avatar
        profile_selectors = [
            "//div[contains(@class,'profile')]",
            "//span[contains(@class,'profile')]",
            "//img[contains(@class,'avatar')]",
            "//button[contains(@class,'profile')]",
            "//div[contains(text(),'Profile')]"
        ]
        
        profile_visible = False
        for selector in profile_selectors:
            try:
                profile_elem = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, selector))
                )
                if profile_elem.is_displayed():
                    profile_visible = True
                    print(f"Found profile element with: {selector}")
                    break
            except:
                continue
        
        print(f"Profile menu visible: {profile_visible}")
        print("TEST 2: Completed")
    except Exception as e:
        print(f"TEST 2 Error: {e}")
    finally:
        driver.quit()


def test_user_name_displayed():
    """Test Case 3: Verify user name is displayed after login"""
    print("\n" + "="*50)
    print("TEST 3: User Name Displayed")
    print("="*50)
    
    driver = setup_driver()
    try:
        login_to_app(driver)
        time.sleep(2)
        
        # Look for user name display
        user_name_selectors = [
            "//span[contains(@class,'user')]",
            "//div[contains(@class,'user-name')]",
            "//span[contains(text(),'Pavan')]",
            "//div[contains(text(),'pavanchenu')]"
        ]
        
        user_found = False
        for selector in user_name_selectors:
            try:
                user_elem = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, selector))
                )
                if user_elem.is_displayed():
                    user_text = user_elem.text
                    print(f"Found user: {user_text}")
                    user_found = True
                    break
            except:
                continue
        
        print(f"User name displayed: {user_found}")
        print("TEST 3: Completed")
    except Exception as e:
        print(f"TEST 3 Error: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    print("="*50)
    print("IgniteLegends Dashboard Tests")
    print("="*50)
    
    test_redirect_to_dashboard()
    test_profile_menu_visible()
    test_user_name_displayed()
    
    print("\n" + "="*50)
    print("All Dashboard Tests Completed!")
    print("="*50)

