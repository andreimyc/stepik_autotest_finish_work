import time
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "testpassword123"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/")
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_success_message()
        page.should_contain_product_name_in_success_message()
        page.should_contain_product_price_in_basket_total_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_contain_product_name_in_success_message()
    page.should_contain_product_price_in_basket_total_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/")
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/")
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/")
    page.open()
    page.add_to_basket()
    page.should_success_message_disappear()
