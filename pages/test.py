from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
browser = webdriver.Chrome()
browser.get(link)
btn = browser.find_element(By.XPATH, ".//button[@value = 'Add to basket']")
price = browser.find_element(By.XPATH, "1").text
name = browser.find_element(By.XPATH, "//*[@class ='col-sm-6 product_main']/h1").text
nameadded = browser.find_element(By.XPATH, "//*[@class ='alertinner ']/strong[text()='Coders at Work']")
priceadded = browser.find_element(By.XPATH, "//*[@class ='alertinner ']/p[1]/strong")
btn.click()

print(name, price)


#assert browser.current_url.find("login") != -1, "URL is not contain Login"