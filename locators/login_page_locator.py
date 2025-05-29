from selenium.webdriver.common.by import By

class LoginPageLocator:
    BUT_FORGOT_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')
    BUT_LOGIN = (By.XPATH,'//button[contains(text(), "Войти")]')
    FIELD_EMAIL = (By.XPATH, '//input[@name="name"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@name="Пароль"]')