import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage

CATALOG_URL = 'http://selenium1py.pythonanywhere.com/catalogue'


def test_guest_should_see_add_to_basket_btn(browser):
    link = f'{CATALOG_URL}/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()


@pytest.mark.parametrize('offer_number',
                         [*range(7),
                          pytest.param(7, marks=pytest.mark.xfail),
                          8, 9])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f'{CATALOG_URL}/coders-at-work_207/?promo=offer{offer_number}'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()


@pytest.mark.skip(reason='Success message is visible now')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f'{CATALOG_URL}/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f'{CATALOG_URL}/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip(reason='Success message do not disappear now')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f'{CATALOG_URL}/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = f'{CATALOG_URL}/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = f'{CATALOG_URL}/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
