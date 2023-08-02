from utilities.logger import Logger
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class LoginPage(Base):

    url = 'https://www.saucedemo.com/'
    username = 'standard_user'
    password = 'secret_sauce'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    USERNAME = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    BUTTON_LOGIN = (By.XPATH, '//*[@id="login-button"]')
    MAIN_WORD = (By.XPATH, '//span[@class="title"]')

    # Getters
    def get_username(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.USERNAME))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PASSWORD))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BUTTON_LOGIN))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.MAIN_WORD))

    # Actions

    def input_username(self, username):
        self.get_username().send_keys(username)
        print('Input username')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')


    # Methods
    def authorization(self):
        with allure.step('authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_username(self.username)
            self.input_password(self.password)
            self.click_login_button()
            self.assert_word(self.get_main_word(),'Products')
            Logger.add_end_step(self.driver.current_url, 'authorization')
