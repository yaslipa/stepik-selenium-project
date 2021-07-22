from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = By.ID, 'login_link'
    LOGIN_LINK_INVALID = By.ID, 'login_link_inc'


class LoginPageLocators:
    LOGIN_FORM = By.ID, 'login_form'
    REGISTER_FORM = By.ID, 'register_form'


class ProductPageLocators:
    ADD_TO_BASKET_BTN = By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket'
    PRODUCT_NAME = By.CSS_SELECTOR, '.product_page h1'
    PRODUCT_PRICE = By.CSS_SELECTOR, '.product_page .price_color'
    SUCCESS_MESSAGE = By.CSS_SELECTOR, '#messages .alert-success'
    SUCCESS_MESSAGE_PRODUCT_NAME = By.CSS_SELECTOR, '#messages .alert-success strong'
    SUCCESS_MESSAGE_PRODUCT_PRICE = By.CSS_SELECTOR, '#messages .alert-info strong'
