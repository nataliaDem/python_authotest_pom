from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.ID, "id_registration-password2")
    REGISTER_BTN =(By.CSS_SELECTOR, "#register_form .btn")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_CART = (By.CSS_SELECTOR, "#messages .alert:first-child strong")
    PRICE_CART = (By.CSS_SELECTOR, "#messages .alert:last-child strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    NO_ITEMS_MESSAGE = (By.CSS_SELECTOR, "#promotions")
    ITEMS_CONTAINER = (By.CSS_SELECTOR, ".basket-items")
