from pageObjects.LoginPage import LoginPage
from utilities.BaseTest import BaseTest
from utilities.TestData import TestData


class Test_001_Login(BaseTest):

    def test_homepage_title(self):
        self.logger = self.get_logger()  # get_logger is designed in base test class
        self.logger.info('******************Test_001_Login****************')
        self.logger.info('*************verifying home page title***********')
        actual_title = self.driver.title

        if actual_title == 'Your store. Login':
            assert True
            self.logger.info('*************home page title test is passed')
        else:
            self.driver.save_screenshot('../Reports/test_homePageTitle.png')
            self.logger.error('***************home page title test is failed*************')
            assert False

    def test_login(self):
        self.logger = self.get_logger()
        self.logger.info('************verifying login test')
        # create an object of LoginPage Class and access its methods
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USERNAME, TestData.PASSWORD)

        actual_title = self.driver.title

        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
            self.logger.info('***********login test is passed************')
        else:
            self.driver.save_screenshot('..\\Reports\\' + 'test_loginPageTitle.png')
            self.logger.error('***************login test is failed**************')
            assert False
