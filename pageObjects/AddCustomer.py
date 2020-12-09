import time
from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage


class AddCustomer(BasePage):
    """By locators"""
    CUSTOMER_MENU = (By.CSS_SELECTOR, 'li.treeview i.fa-user')
    CUSTOMER_SUBMENU = (By.XPATH, "//span[@class='menu-item-title'][(text()='Customers')]")
    ADD_NEW_BUTTON = (By.XPATH, "//a[@class='btn bg-blue']")
    EMAIL_TEXTBOX = (By.ID, 'Email')
    PASSWORD_TEXTBOX = (By.ID, 'Password')
    FIRSTNAME_TEXTBOX = (By.ID, 'FirstName')
    LASTNAME_TEXTBOX = (By.ID, 'LastName')
    GENDER_MALE_RADIO = (By.ID, 'Gender_Male')
    GENDER_FEMALE_RADIO = (By.ID, 'Gender_Female')
    DOB_CALENDAR = (By.ID, 'DateOfBirth')
    COMPANY_TEXTBOX = (By.ID, 'Company')
    TAX_EXEMPT_CHECK = (By.ID, 'IsTaxExempt')
    CUSTOMER_ROLE_SELECT = (By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/parent::div[@class='k-multiselect-wrap k-floatwrap']")
    CUSTOMER_ROLE_ADMINISTRATOR = (By.XPATH, "//li[contains(text(),'Administrator')]")
    CUSTOMER_ROLE_MODERATOR = (By.XPATH, "//li[contains(text(),'Moderator')]")
    CUSTOMER_ROLE_VENDORS = (By.XPATH, "//li[contains(text(),'Vendors')]")
    CUSTOMER_ROLE_GUESTS = (By.XPATH, "//li[contains(text(),'Guests')]")
    CUSTOMER_ROLE_REGISTERED = (By.XPATH, "//li[contains(text(),'Registered')]")
    DELETE_REGISTERED_ROLE = (By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]")

    VENDOR_SELECT = (By.XPATH, "//*[@id='VendorId']")
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[name=save]')

    CUSTOMER_VALIDATION_MESSAGE = (By.TAG_NAME, 'body')

    CUSTOMER_ROLE_LIST = None

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """method actions"""
    def click_customer_menu(self):
        self.do_click(self.CUSTOMER_MENU)

    def click_customer_submenu(self):
        self.do_click(self.CUSTOMER_SUBMENU)

    def click_add_new_customer(self):
        self.do_click(self.ADD_NEW_BUTTON)

    def fill_new_customer_form(self, email, password, firstname, lastname, gender, dob, company, role, vendor):
        self.do_send_keys(self.EMAIL_TEXTBOX, email)
        self.do_send_keys(self.PASSWORD_TEXTBOX, password)
        self.do_send_keys(self.FIRSTNAME_TEXTBOX, firstname)
        self.do_send_keys(self.LASTNAME_TEXTBOX, lastname)
        if gender == 'Female':
            self.do_click(self.GENDER_FEMALE_RADIO)
        else:
            self.do_click(self.GENDER_MALE_RADIO)
        self.do_send_keys(self.DOB_CALENDAR, dob)
        self.do_send_keys(self.COMPANY_TEXTBOX, company)
        self.do_click(self.TAX_EXEMPT_CHECK)

        #  customer role select
        self.do_click(self.CUSTOMER_ROLE_SELECT)
        time.sleep(3)
        if role == 'Registered':
            self.CUSTOMER_ROLE_LIST = self.CUSTOMER_ROLE_REGISTERED
        elif role == 'Administrator':
            self.CUSTOMER_ROLE_LIST = self.CUSTOMER_ROLE_ADMINISTRATOR
        elif role == 'Vendors':
            self.CUSTOMER_ROLE_LIST = self.CUSTOMER_ROLE_VENDORS
        elif role == 'Forum Moderators':
            self.CUSTOMER_ROLE_LIST = self.CUSTOMER_ROLE_MODERATOR
        else:  # by default guest role is selected, if role = guest, delete registered user role
            self.do_click(self.DELETE_REGISTERED_ROLE)
            self.CUSTOMER_ROLE_LIST = self.CUSTOMER_ROLE_GUESTS
        time.sleep(2)
        # self.do_click(self.CUSTOMER_ROLE_LIST) # normal click not working
        # action_chain = ActionChains(self.driver)  # action chain now working
        # action_chain.click(self.driver.find_element(*self.CUSTOMER_ROLE_LIST)).perform()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.CUSTOMER_ROLE_LIST))  # Javascript click

        self.select_drop_down(self.VENDOR_SELECT, vendor)
        time.sleep(3)
        self.do_click(self.SAVE_BUTTON)

    def get_validation_message(self):
        return self.get_element_text(self.CUSTOMER_VALIDATION_MESSAGE)























