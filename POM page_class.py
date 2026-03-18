from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.ID, "loginBtn")

    # Actions
    def enter_username(self, user):
        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(user)

    def enter_password(self, pwd):
        self.wait.until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(pwd)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        ).click()

    def login(self, user, pwd):
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_login()
