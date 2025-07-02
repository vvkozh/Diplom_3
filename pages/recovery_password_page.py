import allure

from curls import Curls
from data import PersonalData
from pages.base_page import BasePage
from locators.login_page_locator import LoginPageLocator
from locators.main_page_locator import MainPageLocator
from locators.recovery_password_page_locator import RecoveryPageLocator

class RecoveryPasswordPage(BasePage):
    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_but_recovery_password(self):
        self.wait_for_element(LoginPageLocator.BUT_FORGOT_PASSWORD)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_on_element(LoginPageLocator.BUT_FORGOT_PASSWORD)

    @allure.step('Клик на кнопку "Восстановить"')
    def click_but_recovery(self):
        self.wait_for_element(RecoveryPageLocator.BUT_RECOVERY)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_on_element(RecoveryPageLocator.BUT_RECOVERY)

    @allure.step('Клик на кнопку "показать/скрыть пароль"')
    def click_show_hide_password(self):
        self.wait_for_element(RecoveryPageLocator.BUT_SHOW_HIDE_PASSWORD)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_on_element(RecoveryPageLocator.BUT_SHOW_HIDE_PASSWORD)

    @allure.step('Заполнить поле email')
    def send_field_email(self):
        self.wait_for_element(RecoveryPageLocator.FIELD_EMAIL)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.send_text_to_input(RecoveryPageLocator.FIELD_EMAIL, PersonalData.EMAIL)

    @allure.step('Подождать загрузки страницы восстановления пароля')
    def wait_loading_page_recovery(self):
        self.wait_for_element(RecoveryPageLocator.FIELD_EMAIL)

    @allure.step('Подождать загрузки страницы сброса пароля')
    def wait_loading_page_reset(self):
        self.wait_for_element(RecoveryPageLocator.BUT_SHOW_HIDE_PASSWORD)

    @allure.step('Переход на страницу авторизации')
    def going_page_login(self):
        self.going_url(Curls.LOGIN_URL)

    @allure.step('Переход на страницу восстановления пароля')
    def going_page_recovery_password(self):
        self.going_url(Curls.FORGOT_PASSWORD_URL)

    @allure.step('сс текущего URL страницы')
    def get_url_page(self):
        return self.get_url()

    @allure.step('Получить атрибута поля "Пароль"')
    def get_attribute_field(self, locator, attribute):
        return self.get_attribute_on_element(locator, attribute)
