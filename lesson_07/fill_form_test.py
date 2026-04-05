import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from Objects.FillForm import FormPage


@pytest.fixture
def driver():
    driver_path = r"C:\Users\Елена\Desktop\Python\lesson_07\msedgedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()
