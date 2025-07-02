from selenium.webdriver.common.by import By

class PersonalAccountPageLocator:
    TEXT_CHANGE_DATA = (By.XPATH, '//p[contains(text(), "В этом разделе вы можете изменить свои персональные данные")]')
    BUT_ORDER_HISTORY = (By.XPATH, '//a[contains(text(), "История заказов")]')
    BUT_EXIT = (By.XPATH, '//button[contains(text(), "Выход")]')
    ACTIVE_BUT_HISTORY = (By.XPATH, '//a[contains(@class, "Account_link_active__2opc9") and contains(text(), "История заказов")]')
    LAST_ORDER_IN_HISTORY = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"][last()]/a[@class="OrderHistory_link__1iNby"]')