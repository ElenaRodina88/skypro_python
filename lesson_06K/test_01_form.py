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


def test_fill_form(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    waiter = WebDriverWait(driver, 20)

    waiter.until(EC.presence_of_element_located((By.NAME, 'first-name'))).send_keys('Иван')
    waiter.until(EC.presence_of_element_located((By.NAME, 'last-name'))).send_keys('Петров')
    waiter.until(EC.presence_of_element_located((By.NAME, 'address'))).send_keys('Ленина, 55-3')
    waiter.until(EC.presence_of_element_located((By.NAME, 'zip-code'))).clear()
    waiter.until(EC.presence_of_element_located((By.NAME, 'city'))).send_keys('Москва')
    waiter.until(EC.presence_of_element_located((By.NAME, 'country'))).send_keys('Россия')
    waiter.until(EC.presence_of_element_located((By.NAME, 'e-mail'))).send_keys('test@skypro.com')
    waiter.until(EC.presence_of_element_located((By.NAME, 'phone'))).send_keys('+7985899998787')
    waiter.until(EC.presence_of_element_located((By.NAME, 'job-position'))).send_keys('QA')
    waiter.until(EC.presence_of_element_located((By.NAME, 'company'))).send_keys('SkyPro')

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    zip_code_field = driver.find_element(By.ID, 'zip-code')
    assert 'alert-danger' in zip_code_field.get_attribute('class')

    fields = [
        'first-name',
        'last-name',
        'address',
        'e-mail',
        'phone',
        'city',
        'country',
        'job-position',
        'company',
    ]

    for field_name in fields:
        field = driver.find_element(By.ID, field_name)
        assert 'alert-success' in field.get_attribute('class')
