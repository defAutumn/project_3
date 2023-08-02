import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.payment_page import PaymentPage
from pages.finish_page import FinishPage



def test_by_product():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print('Start test')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = ClientInformationPage(driver)
    cip.input_inforamtion()

    pp = PaymentPage(driver)
    pp.click_finish_button()

    fp = FinishPage(driver)
    fp.finish()

    print('Success Test!!!')
    driver.quit()


