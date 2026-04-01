import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_total_price(driver):
    driver.get('https://www.saucedemo.com/')

    waiter = WebDriverWait(driver, 10)

    waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#user-name'))).send_keys('standard_user')
    waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#password'))).send_keys('secret_sauce')
    waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button'))).click()

    waiter.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
    waiter.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'))).click()
    waiter.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-onesie'))).click()

    waiter.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))).click()

    waiter.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

    waiter.until(EC.element_to_be_clickable((By.ID, 'first-name'))).send_keys('Ivan')
    waiter.until(EC.element_to_be_clickable((By.ID, 'last-name'))).send_keys('Ivanov')
    waiter.until(EC.element_to_be_clickable((By.ID, 'postal-code'))).send_keys('123456')
    waiter.until(EC.element_to_be_clickable((By.ID, 'continue'))).click()

    total_price = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    price_only = total_price.replace('Total: ', '')

    assert price_only == '$58.29'
