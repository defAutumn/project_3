from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time


def test_by_product():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print('Start test')

    login = LoginPage(driver)
    login.authorization()

    enter_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]')))
    enter_cart.click()
    print('Click Enter Cart')

    print('Success Test!!!')
    driver.quit()


