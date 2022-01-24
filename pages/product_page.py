from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basketball(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        btn.click()

    def should_be_confirmation_message_with_bookname(self):
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        bookadded = self.browser.find_element(*ProductPageLocators.ADDED_BOOK).text
        assert book == bookadded, f"There are no confirmation window with book name - {book}"
        print(book, bookadded)

    def should_be_equal_price(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        priceadded = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        assert price == priceadded, f"Price of the book {price} is not equal to total price {priceadded}"
        print(price, priceadded)
