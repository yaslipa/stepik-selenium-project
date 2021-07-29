from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = By.ID, 'login_link'
    LOGIN_LINK_INVALID = By.ID, 'login_link_inc'
    BASKET_LINK = By.CSS_SELECTOR, '.basket-mini .btn'
    USER_ICON = By.CSS_SELECTOR, '.icon-user'


class BasketPageLocators:
    BASKET_FORM = By.ID, 'basket_formset'
    BASKET_EMPTY_MESSAGE = By.CSS_SELECTOR, '#content_inner > p'


class LoginPageLocators:
    LOGIN_FORM = By.ID, 'login_form'
    REGISTER_FORM = By.ID, 'register_form'
    REGISTER_DATA = (
        (By.ID, 'id_registration-email'),
        (By.ID, 'id_registration-password1'),
        (By.ID, 'id_registration-password2'),
        (By.CSS_SELECTOR, '#register_form button')
    )


class ProductPageLocators:
    ADD_TO_BASKET_BTN = By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket'
    PRODUCT_NAME = By.CSS_SELECTOR, '.product_page h1'
    PRODUCT_PRICE = By.CSS_SELECTOR, '.product_page .price_color'
    SUCCESS_MESSAGE = By.CSS_SELECTOR, '#messages .alert-success'
    SUCCESS_MESSAGE_PRODUCT_NAME = By.CSS_SELECTOR, '#messages .alert-success strong'
    SUCCESS_MESSAGE_PRODUCT_PRICE = By.CSS_SELECTOR, '#messages .alert-info strong'
