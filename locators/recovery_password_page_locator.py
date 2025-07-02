from selenium.webdriver.common.by import By

class RecoveryPageLocator:
    HEAD_RECOVERY_PASSWORD = (By.XPATH, '//h2[.="Восстановление пароля"]')
    FIELD_EMAIL = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')
    BUT_RECOVERY = (By.XPATH, '//button[.="Восстановить"]')
    BUT_SHOW_HIDE_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    ACTIVE_FIELD_PASSWORD = (By.XPATH, '//label[contains(text(), "Пароль")]/ancestor::div[contains(@class, "input_type")]')