from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add-to-basket button is not presented"