from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage


class LoginPage(BasePage):
    # By locators tuples
    USERNAME_TEXTBOX = (By.ID, 'Email')
    PASSWORD_TEXTBOX = (By.ID, 'Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input.login-button')
    LOGOUT_LINK = (By.LINK_TEXT, 'Logout')

# constructor - it will automatically invoked at the time of object creation
    def __init__(self, driver):  # the driver come from testcase
        super().__init__(driver)  # will run the constructor on super class(BasePage) and that will initialise driver

# action method

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME_TEXTBOX, username)
        self.do_send_keys(self.PASSWORD_TEXTBOX, password)
        self.do_click(self.LOGIN_BUTTON)

    def click_logout(self):
        self.do_click(self.LOGOUT_LINK)





