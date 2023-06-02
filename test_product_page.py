import pytest
from selenium import webdriver
from pages.product_page import ProductPage

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.fixture
def link():
    yield "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
def test_guest_can_add_product_to_basket(browser, link):
    # Создаем объект страницы товара, передавая ссылку и браузер
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()  # Получаем проверочный код
    product_name = page.get_product_name()
    assert page.is_element_present("div.alertinner strong", product_name), "No success message with product name"
    assert page.is_element_present("div.alertinner p strong", product_name), "No basket total message"


import time
import pytest


# другой код вашего файла

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    browser.get(link)

    # Добавляем товар в корзину
    page = ProductPage(browser, browser.current_url)
    page.add_to_basket()

    # Проверяем, что нет сообщения об успехе
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    browser.get(link)

    # Проверяем, что нет сообщения об успехе
    page = ProductPage(browser, browser.current_url)
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    browser.get(link)

    # Добавляем товар в корзину
    page = ProductPage(browser, browser.current_url)
    page.add_to_basket()

    # Проверяем, что сообщение об успехе исчезает
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message did not disappear"

# другой код вашего файла


