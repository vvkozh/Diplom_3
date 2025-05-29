import allure
import pytest
import helpers
from curls import Curls
from pages.main_page import MainPage


class TestCheckBasicFunction:
    @allure.title('Тест перехода по клику на "Конструктор"')
    def test_click_but_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.going_page_login()
        main_page.click_but_constructor()
        main_page.wait_load_main_page()
        assert main_page.get_url() == Curls.MAIN_URL

    @allure.title('Тест перехода по клику на "Лента заказов"')
    def test_click_but_feed_order(self, driver):
        main_page = MainPage(driver)
        main_page.going_main_page()
        main_page.click_but_feed_order()
        main_page.wait_load_page_feed_order()
        assert main_page.get_url() == Curls.FEED_URL

    @pytest.mark.parametrize('category', ['buns', 'souses','toppings'])
    @allure.title('Тест клика на ингредиент')
    def test_click_ingredient(self, driver, category):
        locator = helpers.get_ingredient(category)
        main_page = MainPage(driver)
        main_page.going_main_page()
        main_page.scroll_to_element_page(locator[1])
        main_page.click_ingredient(locator[1])
        main_page.wait_load_card_ingredient()
        assert Curls.INGREDIENT_LINK[category][locator[0]] in main_page.get_url_page()

    @pytest.mark.parametrize('category', ['buns', 'souses','toppings'])
    @allure.title('Тест закрытия карточки ингредиента по клику на крестик')
    def test_click_close_card_ingredient(self, driver, category):
        main_page = MainPage(driver)
        main_page.open_card_ingredient(category)
        main_page.click_but_cross()
        assert main_page.wait_hide_card_ingredient()

    @pytest.mark.parametrize('category', ['buns', 'souses', 'toppings'])
    @allure.title('Тест добавление ингредиента и увеличение каунтера')
    def test_add_ingredient(self, driver, category):
        main_page = MainPage(driver)
        main_page.going_main_page()
        locator = main_page.get_locator_ingredient(category)
        old_count = main_page.get_count_element(locator[1])
        main_page.drag_and_drop_ingredient(locator[1])
        new_count = main_page.get_count_element(locator[1])
        assert old_count < new_count

    @allure.title('Тест оформления заказа')
    def test_create_order(self, login_driver):
        main_page = MainPage(login_driver)
        main_page.add_ingredient_in_burger()
        main_page.click_but_create_order()
        assert main_page.wait_load_order_card()