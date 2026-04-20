from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Страница оформления заказа на сайте https://www.saucedemo.com/"""

    def __init__(self, driver):
        """Инициализирует страницу оформления заказа

        Параметры:
            driver: WebDriver браузера

        Ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполняет форму доставки и нажимает "Продолжить"

        Параметры:
            first_name (str): имя
            last_name (str): фамилия
            postal_code (str): почтовый индекс

        Ничего не возвращает.
        """
        self.wait.until(EC.element_to_be_clickable((By.ID, "first-name"))).send_keys(first_name)
        self.wait.until(EC.element_to_be_clickable((By.ID, "last-name"))).send_keys(last_name)
        self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code"))).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def get_total_price(self) -> str:
        """Получает итоговую сумму заказа

        Возвращает:
            str: сумма без текста "Total: " (например, "$58.29")
        """
        total_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        total_text = total_element.text
        return total_text.replace("Total: ", "")
