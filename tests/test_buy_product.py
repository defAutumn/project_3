import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.payment_page import PaymentPage
from pages.finish_page import FinishPage


# @pytest.mark.run(order=2)
def test_buy_product_1(set_up):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print('Start test #1')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_1()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = ClientInformationPage(driver)
    cip.input_information()

    pp = PaymentPage(driver)
    pp.click_finish_button()

    fp = FinishPage(driver)
    fp.finish()

    print('Success Test #1!!!')
    driver.quit()

# @pytest.mark.run(order=3)
# def test_buy_product_2():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     print('Start test #2')
#
#     login = LoginPage(driver)
#     login.authorization()
#
#     mp = MainPage(driver)
#     mp.select_product_2()
#
#     cp = CartPage(driver)
#     cp.product_confirmation()
#
#     print('Success Test #2!!!')
#     driver.quit()
#
# @pytest.mark.run(order=1)
# def test_buy_product_3():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     print('Start test #3')
#
#     login = LoginPage(driver)
#     login.authorization()
#
#     mp = MainPage(driver)
#     mp.select_product_3()
#
#     cp = CartPage(driver)
#     cp.product_confirmation()
#
#     print('Success Test #3!!!')
#     driver.quit()


