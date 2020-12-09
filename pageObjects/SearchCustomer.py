from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage


class SearchCustomer(BasePage):
    """By locators"""
    EMAIL_TEXTBOX = (By.CSS_SELECTOR, "input[id='SearchEmail']")
    FIRSTNAME_TEXTBOX = (By.CSS_SELECTOR, "input[id='SearchFirstName']")
    LASTNAME_TEXTBOX = (By.CSS_SELECTOR, "input[id='SearchLastName']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[id='search-customers']")

    TABLE_ROWS = (By.XPATH, "//table[@id='customers-grid']/tbody/tr")

    TABLE_EMAIL_COLS = (By.XPATH, "//table[@id='customers-grid']/tbody/tr/td[2]")
    TABLE_NAME_COLS = (By.XPATH, "//table[@id='customers-grid']/tbody/tr/td[3]")

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """action methods"""
    def set_customer_email(self, email):
        self.do_send_keys(self.EMAIL_TEXTBOX, email)

    def set_firstname(self, firstname):
        self.do_send_keys(self.FIRSTNAME_TEXTBOX, firstname)

    def set_lastname(self, lastname):
        self.do_send_keys(self.LASTNAME_TEXTBOX, lastname)

    def click_search(self):
        self.do_click(self.SEARCH_BUTTON)

    def get_number_of_rows(self):
        return self.get_length(self.TABLE_ROWS)

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1, self.get_number_of_rows()+1):
            if email == self.get_element_text(self.TABLE_EMAIL_COLS):
                flag = True
                break
        return flag

    def search_customer_by_name(self, firstname, lastname):
        flag = False
        for r in range(1, self.get_number_of_rows()+1):
            if firstname + ' ' + lastname == self.get_element_text(self.TABLE_NAME_COLS):
                flag = True
                break
        return flag







