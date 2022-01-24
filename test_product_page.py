from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basketball()
    page.solve_quiz_and_get_code()
    page.should_be_confirmation_message_with_bookname()
    page.should_be_equal_price()
    #time.sleep(1360)
