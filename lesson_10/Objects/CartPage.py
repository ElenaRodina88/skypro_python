from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Страница корзины на сайте https://www.saucedemo.com/"""

    def __init__(self, driver):
        """Инициализирует страницу корзины

        Параметры:
            driver: WebDriver браузера

        Ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_cart_items(self) -> bool:
        """Проверяет, что в корзине ровно 3 товара

        Возвращает:
            bool: True если товаров 3, иначе False
        """
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items) == 3

    def click_checkout(self) -> None:
        """Нажимает кнопку "Checkout" (Оформить заказ)"""
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
