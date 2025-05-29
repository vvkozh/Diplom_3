import pytest
from selenium import webdriver
from curls import Curls
from data import PersonalData
from locators.login_page_locator import LoginPageLocator
from locators.main_page_locator import MainPageLocator
from pages.base_page import BasePage


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def login_driver(driver):
    login_driver = BasePage(driver)
    login_driver.going_url(Curls.LOGIN_URL)
    login_driver.wait_hide_element(MainPageLocator.OVERLAY)
    login_driver.send_text_to_input(LoginPageLocator.FIELD_EMAIL, PersonalData.EMAIL)
    login_driver.send_text_to_input(LoginPageLocator.FIELD_PASSWORD, PersonalData.PASSWORD)
    login_driver.click_on_element(LoginPageLocator.BUT_LOGIN)
    login_driver.wait_for_element(MainPageLocator.TEXT_COLLECT_BURGER)
    return driver
