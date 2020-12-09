from pageObjects.AddCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.BaseTest import BaseTest
from utilities.TestData import TestData


class Test_003_AddCustomer(BaseTest):

    def test_add_customer(self):
        self.logger = self.get_logger()  # get_logger is designed in base test class
        self.logger.info('******************Test_003_Add Customer****************')
        self.logger.info('*************verifying home page title***********')
        # create object of login page
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USERNAME, TestData.PASSWORD)

        self.logger.info('************login successful**********')
        self.logger.info('************starting add customer ******')

        # creating AddCustomer Object
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_customer_menu()
        self.add_customer.click_customer_submenu()
        self.add_customer.click_add_new_customer()
        self.logger.info('************add customer form  ******')
        self.add_customer.fill_new_customer_form(*TestData.FORM_DATA)
        self.logger.info('************Customer has been created ******')
        self.logger.info('************Customer validation ******')

        if TestData.VALIDATION_MESSAGE in self.add_customer.get_validation_message():
            assert True
            self.logger.info('************Customer validation successful******')
        else:
            self.driver.save_screenshot('../Reports/test_CustomerAdd.png')
            self.logger.error('************Customer validation failed******')
            assert False



        
        







