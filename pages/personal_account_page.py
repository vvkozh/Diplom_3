import allure

from locators.main_page_locator import MainPageLocator
from pages.base_page import BasePage
from locators.personal_account_page_locator import PersonalAccountPageLocator

class PersonalAccountPage(BasePage):
    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_but_personal_account(self):
        self.wait_for_element(MainPageLocator.BUT_PERSONAL_ACCOUNT)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_on_element(MainPageLocator.BUT_PERSONAL_ACCOUNT)

    @allure.step('Клик на последний заказ в "История заказов"')
    def click_on_last_order(self):
        self.wait_for_element(PersonalAccountPageLocator.LAST_ORDER_IN_HISTORY)
        self.scroll_to_element(PersonalAccountPageLocator.LAST_ORDER_IN_HISTORY)
        self.click_on_element(PersonalAccountPageLocator.LAST_ORDER_IN_HISTORY)

    @allure.step('Клик на кнопку')
    def click_but(self, locator):
        self.wait_for_element(locator)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_on_element(locator)

    @allure.step('Получить текущий URL страницы')
    def get_url_page(self):
        return self.get_url()

    @allure.step('Подождать загрузку страницы профиля')
    def wait_load_page_personal_account(self):
        self.wait_for_element(PersonalAccountPageLocator.TEXT_CHANGE_DATA)

    @allure.step('Подождать загрузку страницы')
    def wait_load_page(self, locator):
        return self.wait_for_element(locator)