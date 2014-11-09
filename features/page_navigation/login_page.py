from nose import tools
from selenium.webdriver.common.by import By


def assert_that_current_page_is_login_page(browser):
    current_page_name = browser.find_element(By.NAME, 'page_name').text
    tools.assert_equal('Login', current_page_name)


def login(browser, username, password):
    input_field = browser.find_element(By.NAME, 'username')
    input_field.send_keys(username)
    input_field = browser.find_element(By.NAME, 'password')
    input_field.send_keys(password)
    browser.find_element(By.NAME, 'login').click()
