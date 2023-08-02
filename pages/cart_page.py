import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    CHECKOUT_BUTTON = (By.XPATH, '//button[@id="checkout"]')

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click checkout button')

    # Methods

    def product_confirmation(self):
        with allure.step('product_confirmation'):
            Logger.add_start_step(method='product_confirmation')
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(self.driver.current_url, 'product_confirmation')
