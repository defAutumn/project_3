import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.login_page import LoginPage
from pages.main_page import MainPage



def test_by_product():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print('Start test')

    login = LoginPage(driver)
    login.authorization()
    time.sleep(5)
    mp = MainPage(driver)
    mp.select_product()
    time.sleep(5)
    print('Success Test!!!')
    driver.quit()


