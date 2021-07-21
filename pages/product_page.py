from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_btn()
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()
        self.should_be_success_alert_msg()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BTN
        ), 'Basket button is not presented'

    def should_be_success_alert_msg(self):
        self.should_be_correct_product_name()
        self.should_be_correct_product_price()

    def get_product_name(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME
        ), 'Product name is not presented in product description'
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text

    def get_alert_msg_product_name(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_MSG_PRODUCT_NAME
        ), 'Product name is not presented in alert message'
        return self.browser.find_element(
            *ProductPageLocators.ALERT_MSG_PRODUCT_NAME).text

    def should_be_correct_product_name(self):
        product_name = self.get_product_name()
        alert_msg_product_name = self.get_alert_msg_product_name()
        assert product_name == alert_msg_product_name, 'Wrong product name'

    def get_product_price(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE
        ), 'Product price is not presented in product description'
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text

    def get_alert_msg_product_price(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_MSG_PRODUCT_PRICE
        ), 'Product price is not presented in alert message'
        return self.browser.find_element(
            *ProductPageLocators.ALERT_MSG_PRODUCT_PRICE).text

    def should_be_correct_product_price(self):
        product_price = self.get_product_price()
        alert_msg_product_price = self.get_alert_msg_product_price()
        assert product_price == alert_msg_product_price, 'Wrong product price'
