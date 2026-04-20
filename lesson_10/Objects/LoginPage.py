"""
Содержит класс LoginPage с методами для открытия страницы и выполнения авторизации.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Представляет страницу входа https://www.saucedemo.com/"""

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу входа

        Параметры:
            driver (WebDriver): экземпляр Selenium WebDriver

        Ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открывает страницу входа https://www.saucedemo.com/
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию на странице входа.
        Ждет кликабельности полей username, password и кнопки login,
        заполняет форму и нажимает кнопку входа.

        Параметры:
            username (str): логин пользователя
            password (str): пароль пользователя

        Ничего не возвращает.
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name"))).send_keys(username)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button"))).click()
