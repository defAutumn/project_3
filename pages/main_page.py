from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    SELECT_PRODUCT_1 = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    CART = (By.XPATH, '//div[@id="shopping_cart_container"]')
    BURGER_MENU = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    LINK_ABOUT = (By.XPATH, '//a[@id="about_sidebar_link"]')

    # Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SELECT_PRODUCT_1))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CART))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BURGER_MENU))

    def get_link_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LINK_ABOUT))



    # Actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print('Click add product 1')

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print('Click burger menu')

    def click_link_about(self):
        self.get_link_about().click()
        print('Click link about')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')


    # Methods
    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_burger_menu()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')

