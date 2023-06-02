import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")  # Получение значения аргумента language из командной строки
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    # Установка языка браузера
    browser.get(f"http://example.com/{language}")  # Здесь вы можете использовать нужный URL для установки языка
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Specify the language for the tests")

@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("--language")

import pytest

def pytest_addoption(parser):
    parser.addoption("--promo_offer", action="store", default=None, help="Promo offer for the test")

@pytest.fixture
def promo_offer(request):
    return request.config.getoption("--promo_offer")

