from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")

class BasketPageLocators():
    ALERTS = (By.CSS_SELECTOR, ".alertinner strong")
