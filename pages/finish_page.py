import allure
from base.base_class import Base
from utilities.logger import Logger


class FinishPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # Getters

    # Actions

    # Methods

    def finish(self):
        with allure.step('finish'):
            Logger.add_start_step(method='finish')
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            self.get_screenshot()
            Logger.add_end_step(self.driver.current_url, 'finish')
