import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculate(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    waiter = WebDriverWait(driver, 60)

    delay_input = waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#delay')))
    delay_input.clear()
    delay_input.send_keys('45')

    waiter.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='7']"))).click()
    waiter.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'btn-outline-success') and text()='+']"))).click()
    waiter.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='8']"))).click()
    waiter.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'btn-outline-warning') and text()='=']"))).click()

    waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    assert "15" in driver.find_element(By.CSS_SELECTOR, ".screen").text, 'Результат должен быть равен 15'
