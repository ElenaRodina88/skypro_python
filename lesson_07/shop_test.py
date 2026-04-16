import pytest
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


def test_total_price(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    goods_page = GoodsPage(driver)
    goods_page.add_backpack()
    goods_page.add_tshirt()
    goods_page.add_onesie()
    goods_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Иванов", "123456")

    total_price = checkout_page.get_total_price()
    assert total_price == "$58.29", f"Ожидали $58.29, получили {total_price}"
