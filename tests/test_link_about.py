import time
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.description('Test link about')
def test_link_about():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print('Start test')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_menu_about()

    print('Success Test!!!')
    driver.quit()


