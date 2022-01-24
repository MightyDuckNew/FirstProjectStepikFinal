from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
browser = webdriver.Chrome()
browser.get(link)
#browser.find_elements(By.ID, "register_form")
#url = browser.current_url.find("loginxui")
assert browser.current_url.find("login") != -1, "URL is not contain Login"