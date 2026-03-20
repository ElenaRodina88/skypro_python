from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

input_username = driver.find_element(By.ID, "username")
input_username.send_keys("tomsmith")

input_password = driver.find_element(By.ID, "password")
input_password.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

success_message = driver.find_element(By.CLASS_NAME, "flash.success")
print("Текст сообщения:", success_message.text)

driver.quit()
