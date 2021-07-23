from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, 'Page url is not basket url'

    def should_be_basket_form(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_FORM
        ), 'Basket form is not presented on Basket page'

    def should_not_be_basket_form(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_FORM
        ), 'Basket form is presented on Basket page, but should not be'

    def should_be_basket_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE
        ), 'Basket empty message is not presented on Basket page'
