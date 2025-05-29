import allure
import pytest
from locators.order_feed_page_locator import OrderFeedLocator
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeed:
    @pytest.mark.parametrize('number', [1, 5, 10])
    @allure.title('Тест клика на заказ')
    def test_click_on_order_in_history_order(self, login_driver, number):
        main_page = MainPage(login_driver)
        main_page.click_but_feed_order()
        order_feed_page = OrderFeedPage(login_driver)
        order_feed_page.wait_load_page_feed_order()
        link_order = order_feed_page.get_link_order(number)
        order_feed_page.click_on_order_in_order_feed(number)
        assert order_feed_page.wait_load_order_card()
        assert link_order in order_feed_page.get_url_page()

    @allure.title('Тест отображения заказов пользователя из '
                  'раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_display_order_history_and_order_feed(self, login_driver):
        main_page = MainPage(login_driver)
        main_page.add_ingredient_in_burger()
        main_page.click_but_create_order()
        main_page.wait_load_order_card()
        order_feed_page = OrderFeedPage(login_driver)
        order_feed_page.going_in_order_history()
        order_href = order_feed_page.get_href_last_order()
        order_feed_page.click_on_last_order()
        expected_id_order = order_feed_page.get_id_last_order()
        order_feed_page.going_in_feed_order()
        order_feed_page.click_order_on_href(order_href)
        actual_id_order = order_feed_page.get_id_last_order()
        assert actual_id_order == expected_id_order

    @pytest.mark.parametrize('locator, name_test',
                             [(OrderFeedLocator.COUNT_ORDERS_ALL_TIME, 'Тест увеличения счетчика "Выполнено за всё время"'),
                             (OrderFeedLocator.COUNT_ORDERS_TODAY, 'Тест увеличения счетчика "Выполнено за сегодня"')])
    def test_count_orders_in_feed_order_page(self, login_driver, locator, name_test):
        allure.dynamic.title(name_test)
        order_feed_page = OrderFeedPage(login_driver)
        order_feed_page.going_in_feed_order()
        old_value = order_feed_page.get_count_orders(locator)
        main_page = MainPage(login_driver)
        main_page.going_main_page()
        main_page.add_ingredient_in_burger()
        main_page.click_but_create_order()
        main_page.wait_load_order_card()
        order_feed_page.going_in_feed_order()
        new_value = order_feed_page.get_count_orders(locator)
        assert old_value < new_value

    @allure.title('Тест появления номера заказа в разделе "В работе" после оформления заказа')
    def test_display_order_(self, login_driver):
        main_page = MainPage(login_driver)
        main_page.add_ingredient_in_burger()
        main_page.click_but_create_order()
        order_id = main_page.wait_load_order_card()
        order_feed_page = OrderFeedPage(login_driver)
        order_feed_page.going_in_feed_order()
        order_feed_page.wait_order_in_work()
        orders_in_work = order_feed_page.get_id_order_in_work()
        assert order_id in orders_in_work