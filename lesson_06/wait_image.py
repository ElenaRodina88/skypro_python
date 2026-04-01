from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 50)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

waiter.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#landscape"))
)

third_image = driver.find_elements(By.TAG_NAME, 'img')[3]
src_value = third_image.get_attribute('src')

print(src_value)

driver.quit()
