from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
browser = webdriver.Chrome()
browser.get(link)
browser.find_elements(By.ID, "register_form")