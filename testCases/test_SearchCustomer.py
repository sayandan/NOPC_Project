import time

from pageObjects.AddCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.BaseTest import BaseTest
from utilities.TestData import TestData


class Test_004_SearchCustomer(BaseTest):

    def test_search_by_email(self):
        self.logger = self.get_logger()  # get_logger is designed in base test class
        self.logger.info('******************Test_003_Add Customer****************')
        self.logger.info('*************verifying home page title***********')
        # create object of login page
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USERNAME, TestData.PASSWORD)

        self.logger.info('************login successful**********')
        self.logger.info('************starting customer menu******')

        # creating AddCustomer Object
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_customer_menu()
        self.add_customer.click_customer_submenu()

        self.logger.info('************searching customer by email **********')
        # create search customer object
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.set_customer_email(TestData.SEARCH_EMAIL)
        time.sleep(3)
        self.search_customer.click_search()
        time.sleep(3)
        assert self.search_customer.search_customer_by_email(TestData.SEARCH_EMAIL)

    def test_search_by_name(self):
        self.logger = self.get_logger()  # get_logger is designed in base test class
        self.logger.info('************searching customer by name **********')
        # create search customer object
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.set_customer_email('')  # clear the email textbox
        self.search_customer.set_firstname(TestData.SEARCH_FIRSTNAME)
        self.search_customer.set_lastname(TestData.SEARCH_LASTNAME)
        time.sleep(3)
        self.search_customer.click_search()
        time.sleep(3)
        assert self.search_customer.search_customer_by_name(TestData.SEARCH_FIRSTNAME, TestData.SEARCH_LASTNAME)







