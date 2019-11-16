from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.locators import BasketPageLocators
import pytest
import time


# @pytest.mark.skip("Параметризованный тест на книгу 'Coders at Work'")
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/"
#                                                "catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket_coders(browser, link):
#
#     page = ProductPage(browser, link)
#     page.open()
#
#     product_name, product_price = page.get_product_info()
#
#     page.should_be_add_to_basket_btn()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_alerts()
#     basket_page.check_product_info(product_name, product_price)
#
#
# def test_guest_can_add_product_to_basket(browser, link="http://selenium1py.pythonanywhere.com/"
#                                                        "catalogue/the-shellcoders-handbook_209/?promo=newYear"):
#
#     page = ProductPage(browser, link)
#     page.open()
#
#     product_name, product_price = page.get_product_info()
#
#     page.should_be_add_to_basket_btn()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_alerts()
#     basket_page.check_product_info(product_name, product_price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket\
                (browser, link="http://selenium1py.pythonanywhere.com/"
                               "catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    page = ProductPage(browser, link)
    page.open()
    page.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message\
                (browser, link="http://selenium1py.pythonanywhere.com/"
                               "catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket\
                (browser, link="http://selenium1py.pythonanywhere.com/"
                               "catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    page = ProductPage(browser, link)
    page.open()
    page.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_disappear()

