import pytest

from pages.product_page import ProductPage

CATALOG_URL = 'http://selenium1py.pythonanywhere.com/catalogue'


@pytest.mark.parametrize('offer_number',
                         [*range(0, 7),
                          pytest.param(7, marks=pytest.mark.xfail),
                          8, 9])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f'{CATALOG_URL}/coders-at-work_207/?promo=offer{offer_number}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


def test_guest_should_see_add_to_basket_btn(browser):
    link = f'{CATALOG_URL}/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
