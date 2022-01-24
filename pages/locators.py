from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "register_form")
    REGISTRATION_FORM = (By.ID, "login_form")

class ProductPageLocators():
    ADD_BTN = (By.XPATH, ".//button[@value = 'Add to basket']")
    BOOK_NAME = (By.XPATH, "//*[@class ='col-sm-6 product_main']/h1")
    BOOK_PRICE = (By.XPATH, "//*[@class ='col-sm-6 product_main']/p[1]")
    ADDED_BOOK = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    TOTAL_PRICE = (By.XPATH, "//*[@class ='alertinner ']/p[1]/strong")
