from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_bth = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_bth.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_price(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_CART).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price == price_basket

    def should_be_correct_name(self):
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_CART).text
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        assert name == name_basket

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.NAME_CART), \
            "Success message is presented"

    def should_disappear_success_message(self):
        assert not self.is_disappeared(*ProductPageLocators.NAME_CART), \
            "Success message disappears"
