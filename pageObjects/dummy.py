from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.TestData import TestData

driver = webdriver.Chrome()
driver.get(TestData.BASE_URL)
driver.find_element_by_id('Email').clear()
driver.find_element_by_id('Email').send_keys(TestData.USERNAME)
driver.find_element_by_id('Password').clear()
driver.find_element_by_id('Password').send_keys(TestData.PASSWORD)
driver.find_element_by_css_selector('input.login-button').click()

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

VENDOR_SELECT = (By.CSS_SELECTOR, 'select#VendorId')
SAVE_BUTTON = (By.CSS_SELECTOR, 'button[name=save]')

driver.find_element(*CUSTOMER_MENU).click()
driver.find_element(*CUSTOMER_SUBMENU).click()
driver.find_element(*ADD_NEW_BUTTON).click()

driver.find_element(*EMAIL_TEXTBOX).send_keys('siva1@gmail.com')
driver.find_element(*PASSWORD_TEXTBOX).send_keys('password')
driver.find_element(*FIRSTNAME_TEXTBOX).send_keys('siva')
driver.find_element(*LASTNAME_TEXTBOX).send_keys('davai')
driver.find_element(*PASSWORD_TEXTBOX).send_keys('password')
driver.find_element(*GENDER_MALE_RADIO).click()
driver.find_element(*DOB_CALENDAR).send_keys('01/01/1980')
driver.find_element(*COMPANY_TEXTBOX).send_keys('Moss')
driver.find_element(*TAX_EXEMPT_CHECK).click()
driver.find_element(*CUSTOMER_ROLE_SELECT).click()
driver.find_element(*CUSTOMER_ROLE_ADMINISTRATOR).click()



# driver.find_element(*SAVE_BUTTON).click()
