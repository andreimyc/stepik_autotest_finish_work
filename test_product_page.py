import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_message()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page (browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/")
#     page.open()
#     page.add_to_basket()
#     # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/")
#     page.open()
#     # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/")
#     page.open()
#     page.add_to_basket()
#     # Проверяем, что сообщение об успехе исчезает с помощью is_disappeared
#     page.should_success_message_disappear()

# @pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     if promo_offer == "7":
#         pytest.xfail("Test intentionally marked as xfail due to known issue")
#     page.should_be_success_message()
#     page.should_contain_product_name_in_success_message()
#     page.should_contain_product_price_in_basket_total_message()
#     page.should_see_as_disappering_message()

# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     product_name = page.get_product_name()
#     product_price = page.get_product_price()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_success_message()
#     page.should_contain_product_name_in_success_message(product_name)
#     page.should_contain_product_price_in_basket_total_message(product_price)
#     # print(f"Product Name: {product_name}")
#     # print(f"Product Price: {product_price}")