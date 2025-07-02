from selenium.webdriver.common.by import By

class OrderFeedLocator:
    ORDER_CARD = (By.XPATH, '//p[text()="Выполнен"]/ancestor::section[contains(@class, "Modal_modal_opened__3ISw4")]')
    ORDER_ID_IN_HISTORY = (By.XPATH, '//p[@class="text text_type_digits-default mb-10 mt-5"]')
    BUT_CLOSE_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4")]//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    COUNT_ORDERS_ALL_TIME = (By.XPATH, '//p[contains(text(), "Выполнено за все время")]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    COUNT_ORDERS_TODAY = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    ORDER_ID_AFTER_PURCHASE = (By.XPATH, '//p[contains(text(), "идентификатор заказа")]/preceding-sibling::h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    ORDER_IN_WORK = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]')
    ORDER_IN_WORK_1 = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]')

    @staticmethod
    def order_history_locator(number):
        return By.XPATH, f'//li[@class="OrderHistory_listItem__2x95r mb-6"][{number}]/a[@class="OrderHistory_link__1iNby"]'