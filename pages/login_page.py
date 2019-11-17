from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Слово login отсутствует в текущей ссылке"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма фхода отсутствует на странице"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует на странице"

    def register_new_user(self, email, password):
        self.input(*LoginPageLocators.REG_EMAIL, value=email)
        self.input(*LoginPageLocators.REG_PASS1, value=password)
        self.input(*LoginPageLocators.REG_PASS2, value=password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()

