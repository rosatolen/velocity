from nose import tools
from selenium.webdriver.common.by import By


def navigate_to_registration_page(context):
    context.browser.get('localhost:1234/register')


def register(browser, username, password, repassword):
    browser.get('localhost:1234/register')
    input_field = browser.find_element(By.NAME, 'username')
    input_field.send_keys(username)
    input_field = browser.find_element(By.NAME, 'password')
    input_field.send_keys(password)
    input_field = browser.find_element(By.NAME, 'retype_password')
    input_field.send_keys(repassword)
    browser.find_element(By.NAME, 'register').click()

