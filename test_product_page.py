import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    if promo_offer == "7":
        pytest.xfail("Test intentionally marked as xfail due to known issue")
    page.should_be_success_message()
    page.should_contain_product_name_in_success_message()
    page.should_contain_product_price_in_basket_total_message()

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