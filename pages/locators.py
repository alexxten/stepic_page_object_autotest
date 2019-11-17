from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = By.CSS_SELECTOR, "#login_form"
    REGISTER_FORM = By.CSS_SELECTOR, "#register_form"


class ProductPageLocators:
    ADD_TO_BASKET_BTN = By.CSS_SELECTOR, ".btn-add-to-basket"
    PRODUCT_NAME = By.CSS_SELECTOR, ".product_main h1"
    PRODUCT_PRICE = By.CSS_SELECTOR, ".price_color"
    SUCCESS_MESSAGE = By.XPATH, "//div[@class='alertinner ']//strong[contains(text(), 'The')]"


class BasketPageLocators:
    ALERTS = By.CSS_SELECTOR, ".alertinner strong"
    CONTENT = By.CSS_SELECTOR, "#content_inner"
    IN_BASKET = By.CSS_SELECTOR, ".basket-mini strong"


class BasePageLocators:
    LOGIN_LINK = By.CSS_SELECTOR, "#login_link"
    LOGIN_LINK_INVALID = By.CSS_SELECTOR, "#login_link_inc"
    BASKET_LINK = By.XPATH, "//a[@class='btn btn-default']"

