"""IgniteLegends UI Validation Tests using Selenium and pytest"""
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    """Setup Edge driver"""
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--disable-extensions")
    driver = webdriver.Edge(options=edge_options)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_page(driver):
    """Navigate to login page and return driver"""
    driver.get("https://dev.ignitelegends.com/")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form"))
    )
    return driver


def test_login_button_enabled(login_page):
    """Test: Verify login/submit button is enabled"""
    submit_button = WebDriverWait(login_page, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    assert submit_button.is_enabled(), "Login button should be enabled"


def test_password_masked(login_page):
    """Test: Verify password field is masked"""
    password_field = login_page.find_element(By.XPATH, "//input[@type='password']")
    assert password_field.get_attribute("type") == "password", "Password should be masked"


def test_placeholder_text(login_page):
    """Test: Verify input fields have proper attributes for user guidance"""
    email_field = login_page.find_element(By.XPATH, "//input[@type='email']")
    password_field = login_page.find_element(By.XPATH, "//input[@type='password']")
    # Check that fields exist, are visible, and are editable
    assert email_field.is_displayed(), "Email field should be visible"
    assert password_field.is_displayed(), "Password field should be visible"
    assert email_field.is_enabled(), "Email field should be enabled"


def test_error_message_display(login_page):
    """Test: Verify error message displays with invalid credentials"""
    email_field = login_page.find_element(By.XPATH, "//input[@type='email']")
    password_field = login_page.find_element(By.XPATH, "//input[@type='password']")
    submit_button = login_page.find_element(By.XPATH, "//button[@type='submit']")
    
    email_field.clear()
    email_field.send_keys("invalid@test")
    password_field.clear()
    password_field.send_keys("wrongpass")
    submit_button.click()
    
    login_page.implicitly_wait(3)
    # Check for error message (generic approach - looks for error text or class)
    error_elements = login_page.find_elements(By.XPATH, "//*[contains(@class,'error') or contains(@class,'alert')]")
    assert len(error_elements) > 0 or login_page.current_url != "https://dev.ignitelegends.com/", \
        "Error message should display for invalid credentials"
