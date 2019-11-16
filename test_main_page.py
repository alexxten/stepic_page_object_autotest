def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    page = ProductPage(browser, link)
    page.open()
    page.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    page = ProductPage(browser, link)
    page.open()
    page.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
    page.solve_quiz_and_get_code()
    page.should_dissapear()