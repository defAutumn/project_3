from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class ClientInformationPage(Base):

    first_name = 'Vitalik'
    last_name = 'Kakoito'
    postal_code = '123456'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FIRST_NAME = (By.XPATH, '//input[@id="first-name"]')
    LAST_NAME = (By.XPATH, '//input[@id="last-name"]')
    ZIP_CODE = (By.XPATH, '//input[@id="postal-code"]')
    BUTTON_CONTINUE = (By.XPATH, '//input[@id="continue"]')

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FIRST_NAME))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LAST_NAME))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ZIP_CODE))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BUTTON_CONTINUE))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name')

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print('Input postal code')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')


    # Methods
    def input_inforamtion(self):
        self.get_current_url()
        self.input_first_name(self.first_name)
        self.input_last_name(self.last_name)
        self.input_zip_code(self.postal_code)
        self.click_continue_button()
        # self.assert_word(self.get_main_word(),'Products')
