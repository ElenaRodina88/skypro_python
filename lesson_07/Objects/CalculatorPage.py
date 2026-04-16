from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay_field = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay_field.clear()
        delay_field.send_keys(seconds)

    def press_digit(self, digit):
        digit_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[contains(@class, 'btn-outline-primary') and text()='{digit}']")))
        digit_btn.click()

    def press_plus(self):
        plus_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class, 'btn-outline-success') and text()='+']")))
        plus_btn.click()

    def press_equals(self):
        equals_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class, 'btn-outline-warning') and text()='=']")))
        equals_btn.click()

    def wait_result(self, timeout=50):

        def calculation_complete(driver):
            screen_text = driver.find_element(By.CSS_SELECTOR, ".screen").text.strip()
            return screen_text.isdigit()

        custom_wait = WebDriverWait(self.driver, timeout)
        custom_wait.until(calculation_complete)

    def get_result(self):
        self.wait_result(50)
        result_field = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_field.text.strip()