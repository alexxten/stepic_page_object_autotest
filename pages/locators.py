from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = By.CSS_SELECTOR, "#login_link"
    LOGIN_LINK_INVALID = By.CSS_SELECTOR, "#login_link_inc"


class LoginPageLocators:
    LOGIN_FORM = By.CSS_SELECTOR, "#login_form"
    REGISTER_FORM = By.CSS_SELECTOR, "#register_form"
    pass


class ProductPageLocators:
    ADD_TO_BASKET_BTN = By.CLASS_NAME, "btn-add-to-basket"
    PRODUCT_NAME = By.CSS_SELECTOR, ".product_main h1"
    PRODUCT_PRICE = By.CLASS_NAME, "price_color"
    SUCCESS_MESSAGE = By.XPATH, "//div[@class='alertinner ']//strong[contains(text(), 'The')]"


class BasketPageLocators:
    ALERTS = By.CSS_SELECTOR, ".alertinner strong"
