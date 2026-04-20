from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoodsPage:
    """Представляет страницу товаров на сайте https://www.saucedemo.com/"""

    def __init__(self, driver):
        """Инициализирует страницу товаров

        Параметры:
            driver: WebDriver браузера

        Ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        """Добавляет рюкзак в корзину"""
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    def add_tshirt(self):
        """Добавляет футболку в корзину"""
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()

    def add_onesie(self):
        """Добавляет боди в корзину"""
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    def go_to_cart(self):
        """Переходит в корзину"""
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
