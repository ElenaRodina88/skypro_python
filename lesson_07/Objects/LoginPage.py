from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name"))).send_keys(username)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button"))).click()
