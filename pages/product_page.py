from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add-to-basket button is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element is presented, but should disappear"

    def get_product_info(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        return name, price

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()