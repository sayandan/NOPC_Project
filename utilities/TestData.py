import random
import string


def random_gen(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class TestData:

    BASE_URL = 'https://admin-demo.nopcommerce.com/'
    USERNAME = 'admin@yourstore.com'
    PASSWORD = 'admin'

    CHROME_EXECUTABLE_PATH = 'c://WebDrivers//chromedriver.exe'
    EDGE_EXECUTABLE_PATH = 'c://WebDrivers//msedgedriver.exe'

    email = random_gen() + '@gmail.com'
    FORM_DATA = [email, 'password12', 'siv', 'last', 'Male', '12/31/1980', 'Moss', 'Guests', 'Vendor 1']

    VALIDATION_MESSAGE = 'The new customer has been added successfully.'

    SEARCH_EMAIL = 'james_pan@nopCommerce.com'
    SEARCH_FIRSTNAME = 'Arthur'
    SEARCH_LASTNAME = 'Holmes'

