# Автоматизация тестирования Saucedemo
Проект автоматизированного тестирования интернет-магазина [Saucedemo](https://www.saucedemo.com/) с использованием Selenium, pytest и Allure отчетов.

## Технологии
- **Python**
- **Selenium WebDriver** (Firefox + GeckoDriver)
- **pytest** - фреймворк тестирования
- **Allure** - генерация отчетов
- **webdriver-manager** - автоматическая установка драйверов
- **Page Object Model** - архитектура страниц

## Запуск тестов и просмотр отчета

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Запуск тестов для формирования отчета
```bash
pytest tests/ --alluredir=allure-results --clean-alluredir
```

### 3. Просмотр отчета
```bash
allure serve allure-results
```
Отчет откроется автоматически в браузере