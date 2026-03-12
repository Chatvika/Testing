import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=options)

    yield driver

    driver.quit()


def test_ecommerce_flow(driver):

    wait = WebDriverWait(driver,10)

    # Open website
    driver.get("https://www.saucedemo.com")

    # Login
    wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    # Verify products page
    title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,"title"))
    ).text

    assert title == "Products"

    # Add product to cart
    wait.until(
        EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack"))
    ).click()

    # Open cart
    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))
    ).click()

    # Verify product in cart
    product = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item_name"))
    ).text

    assert product == "Sauce Labs Backpack"

    # Remove product
    wait.until(
        EC.element_to_be_clickable((By.ID,"remove-sauce-labs-backpack"))
    ).click()

    # Verify cart empty
    cart_items = driver.find_elements(By.CLASS_NAME,"cart_item")
    assert len(cart_items) == 0

    # Open menu
    wait.until(
        EC.element_to_be_clickable((By.ID,"react-burger-menu-btn"))
    ).click()

    # Logout
    wait.until(
        EC.element_to_be_clickable((By.ID,"logout_sidebar_link"))
    ).click()

    # Verify logout page
    login_button = wait.until(
        EC.visibility_of_element_located((By.ID,"login-button"))
    )

    assert login_button.is_displayed()
    