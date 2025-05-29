import allure
import helpers
from curls import Curls
from locators.main_page_locator import MainPageLocator
from locators.personal_account_page_locator import PersonalAccountPageLocator
from pages.base_page import BasePage
from locators.order_feed_page_locator import OrderFeedLocator

class OrderFeedPage(BasePage):
    @allure.step('Клик на заказ на странице "Лента заказов"')
    def click_on_order_in_order_feed(self, number):
        locator = OrderFeedLocator.order_history_locator(number)
        self.wait_for_element(locator)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    @allure.step('Клик на последний заказ в "История заказов"')
    def click_on_last_order(self):
        self.wait_for_element(PersonalAccountPageLocator.LAST_ORDER_IN_HISTORY)
        self.scroll_to_element(PersonalAccountPageLocator.LAST_ORDER_IN_HISTORY)
        self.click_on_element(PersonalAccountPageLocator.LAST_ORDER_IN_HISTORY)

    @allure.step('Клик на заказ из истории заказов')
    def click_order_on_href(self, href):
        end_href = href.split('https://stellarburgers.nomoreparties.site/account/order-history/')[-1]
        order_locator = helpers.get_order_locator(end_href)
        self.wait_for_element(order_locator)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_on_element(order_locator)

    @allure.step('Переход на страницу "История заказов"')
    def going_in_order_history(self):
        self.going_url(Curls.ACCOUNT_URL)
        self.wait_for_element(PersonalAccountPageLocator.BUT_ORDER_HISTORY)
        self.wait_hide_element(MainPageLocator.OVERLAY)
        self.click_on_element(PersonalAccountPageLocator.BUT_ORDER_HISTORY)

    @allure.step('Переход на страницу "Лента заказов"')
    def going_in_feed_order(self):
        self.going_url(Curls.FEED_URL)

    @allure.step('Подождать загрузки карточки заказа')
    def wait_load_order_card(self):
        return self.wait_for_element(OrderFeedLocator.ORDER_CARD)

    @allure.step('Подождать загрузки страницы ленты заказов')
    def wait_load_page_feed_order(self):
        self.wait_for_element(MainPageLocator.TEXT_FEED_ORDER)

    @allure.step('Подождать появления номера заказа в разделе "В работе"')
    def wait_order_in_work(self):
        return self.wait_change_element(OrderFeedLocator.ORDER_IN_WORK_1, 'Все текущие заказы готовы!')

    @allure.step('Получить текущего URL страницы')
    def get_url_page(self):
        return self.get_url()

    @allure.step('Получить атрибута секции карточки ингредиента')
    def get_link_order(self, number):
        locator = OrderFeedLocator.order_history_locator(number)
        return self.get_attribute_on_element(locator, 'href')

    @allure.step('Получить номера последнего заказа')
    def get_id_last_order(self):
        order_id = self.wait_for_element(OrderFeedLocator.ORDER_ID_IN_HISTORY)
        return order_id.text

    @allure.step('Получить количества заказов за все время')
    def get_count_orders(self, locator):
        count_orders = self.wait_for_element(locator)
        return count_orders.text

    @allure.step('Получить атрибут href последнего заказа')
    def get_href_last_order(self):
        return self.get_attribute_on_element(PersonalAccountPageLocator.LAST_ORDER_IN_HISTORY, 'href')

    @allure.step('Получение списка заказов из раздела "В работе"')
    def get_id_order_in_work(self):
        elements = self.wait_load_all_elements(OrderFeedLocator.ORDER_IN_WORK)
        orders_in_work = [element.text for element in elements]
        return orders_in_work