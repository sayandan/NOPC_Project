import time
from pageObjects.LoginPage import LoginPage
from utilities.BaseTest import BaseTest
from utilities import XLUtils


class Test_002_Login_DDT(BaseTest):

    path = '../utilities/LoginData.xlsx'  # path of the EXCEL file
    rows = XLUtils.get_row_count(path, 'Sheet1')  # returns no of rows from excel file
    print(rows)

    def test_login_DDT(self):
        self.logger = self.get_logger()
        self.logger.info('******************Test_002_Login_DDT****************')
        self.logger.info('************verifying login test')
        # create an object of LoginPage Class and access its methods
        self.login_page = LoginPage(self.driver)
        list_status = []  # empty list variable to get the status of the test conditions
        for r in range(2,self.rows+1):  # loops from row 2 to (rows +1) exclusive
            self.user = XLUtils.read_data(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.read_data(self.path, 'Sheet1', r, 2)
            self.expected_value = XLUtils.read_data(self.path, 'Sheet1', r, 3)

            self.login_page.do_login(self.user, self.password)
            # self.login_page.set_username(self.user)
            # self.login_page.set_password(self.password)
            # self.login_page.click_login()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = 'Dashboard / nopCommerce administration'

            if actual_title == expected_title:
                if self.expected_value == 'Pass':
                    list_status.append('Pass')
                    self.logger.info('***********login test is passed************')
                    self.login_page.click_logout()
                elif self.expected_value == 'Fail':
                    self.logger.error('***************login test is failed**************')
                    self.driver.save_screenshot('..\\Reports\\' + 'test_loginPageTitle_DDT.png')
                    list_status.append('Fail')
                    self.login_page.click_logout()
            elif actual_title != expected_title:
                if self.expected_value == 'Fail':
                    list_status.append('Pass')
                    self.logger.info('***********login test is passed************')
                elif self.expected_value == 'Pass':
                    self.logger.error('***************login test is failed**************')
                    self.driver.save_screenshot('..\\Reports\\' + 'test_loginPageTitle_DDT.png')
                    list_status.append('Fail')

        if 'Fail' not in list_status:
            self.logger.info('***********login DDT test is passed************')
            assert True
        else:
            self.logger.info('***********login DDT test is Failed************')
            assert False







