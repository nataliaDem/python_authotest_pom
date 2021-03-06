from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEMS_MESSAGE), \
            "No items in basket message is presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_CONTAINER), \
            "There is no items in basket"
