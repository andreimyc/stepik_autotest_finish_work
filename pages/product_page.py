from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_basket_total_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"

    def should_contain_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == success_message, "Product name does not match the success message"

    def should_contain_product_price_in_basket_total_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == basket_total_message, "The price of the product does not match the success message"

    # def should_contain_product_name_in_success_message(self, expected_product_name):
    #     success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
    #     assert expected_product_name in success_message, "Product name is not in the success message"
    #
    # def should_contain_product_price_in_basket_total_message(self, expected_basket_total):
    #     basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
    #     assert expected_basket_total in basket_total_message, "Basket total is not in the message"
