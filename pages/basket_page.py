from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_alerts(self):
        assert self.are_elements_present(*BasketPageLocators.ALERTS), "Alerts are not presented"

    def check_prod_name(self, prod_name, prod_price, b_prod_name, b_prod_price):
        assert prod_name == b_prod_name, f"Expected {prod_name}, get {b_prod_name}"
        assert prod_price == b_prod_price, f"Expected {prod_price}, get {b_prod_price}"