import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from Objects.LoginPage import LoginPage
from Objects.GoodsPage import GoodsPage
from Objects.CartPage import CartPage
from Objects.CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка итоговой цены заказа")
@allure.description("Авторизация, добавление 3 товаров в корзину, оформление заказа и проверка итоговой суммы $58.29")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_total_price(driver):
    # Шаг 1: Авторизация
    with allure.step("Открываем страницу входа"):
        login_page = LoginPage(driver)
        login_page.open()

    with allure.step("Входим под standard_user"):
        login_page.login("standard_user", "secret_sauce")

    # Шаг 2: Добавление товаров
    with allure.step("Переходим на страницу товаров"):
        goods_page = GoodsPage(driver)

    with allure.step("Добавляем рюкзак в корзину"):
        goods_page.add_backpack()

    with allure.step("Добавляем футболку в корзину"):
        goods_page.add_tshirt()

    with allure.step("Добавляем боди в корзину"):
        goods_page.add_onesie()

    with allure.step("Переходим в корзину"):
        goods_page.go_to_cart()

    # Шаг 3: Оформление заказа
    with allure.step("Нажимаем Checkout"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполняем форму доставки"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Иван", "Иванов", "123456")

    # Проверка
    with allure.step("Проверяем итоговую сумму"):
        total_price = checkout_page.get_total_price()
        assert total_price == "$58.29", f"Ожидали $58.29, получили {total_price}"
