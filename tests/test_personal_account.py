import allure
import pytest
from curls import Curls
from locators.login_page_locator import LoginPageLocator
from locators.personal_account_page_locator import PersonalAccountPageLocator
from pages.personal_account_page import PersonalAccountPage

class TestPersonalAccount:
    @allure.title('Тест перехода по клику на "Личный кабинет"')
    def test_click_personal_account(self, login_driver):
        personal_account_page = PersonalAccountPage(login_driver)
        personal_account_page.click_but_personal_account()
        personal_account_page.wait_load_page_personal_account()
        assert personal_account_page.get_url_page() == Curls.PERSONAL_ACCOUNT_URL

    @pytest.mark.parametrize('locator_for_click, locator_for_wait, expected_result, name_test',
                             [(PersonalAccountPageLocator.BUT_ORDER_HISTORY,
                              PersonalAccountPageLocator.ACTIVE_BUT_HISTORY,
                              Curls.ORDER_HISTORY_URL,
                              'Тест перехода в раздел "История заказов" и выхода из аккаунта'),
                             (PersonalAccountPageLocator.BUT_EXIT,
                              LoginPageLocator.BUT_LOGIN,
                              Curls.LOGIN_URL,
                              'Тест выхода из аккаунта')])
    def test_click_but_exit_and_history(self, login_driver, locator_for_click,
                                        locator_for_wait, expected_result, name_test):
        allure.dynamic.title(name_test)
        personal_account_page = PersonalAccountPage(login_driver)
        personal_account_page.click_but_personal_account()
        personal_account_page.wait_load_page_personal_account()
        personal_account_page.click_but(locator_for_click)
        personal_account_page.wait_load_page(locator_for_wait)
        assert personal_account_page.get_url_page() == expected_result