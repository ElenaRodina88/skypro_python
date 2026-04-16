import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Objects.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calculator = CalculatorPage(driver)

    calculator.open()
    calculator.set_delay("45")
    calculator.press_digit("7")
    calculator.press_plus()
    calculator.press_digit("8")
    calculator.press_equals()

    result = calculator.get_result()
    assert result == "15", f"Ожидаем 15, получаем {result}"
