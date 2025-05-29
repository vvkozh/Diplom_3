import allure
from curls import Curls
from locators.recovery_password_page_locator import RecoveryPageLocator
from pages.recovery_password_page import RecoveryPasswordPage

class TestRecoveryPassword:
    @allure.title('Тест перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_click_recovery_button(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.going_page_login()
        recovery_password_page.click_but_recovery_password()
        recovery_password_page.wait_loading_page_recovery()
        assert recovery_password_page.get_url_page() == Curls.FORGOT_PASSWORD_URL

    @allure.title('Тест ввода почты и клик по кнопке "Восстановить"')
    def test_send_email_and_click_recovery(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.going_page_recovery_password()
        recovery_password_page.send_field_email()
        recovery_password_page.click_but_recovery()
        recovery_password_page.wait_loading_page_reset()
        assert recovery_password_page.get_url_page() == Curls.RESET_PASSWORD_URL

    @allure.title('Тест подсвечивания поля "пароль" после клика по кнопке "показать/скрыть пароль"')
    def test_click_but_show_hide_password(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.going_page_recovery_password()
        recovery_password_page.send_field_email()
        recovery_password_page.click_but_recovery()
        recovery_password_page.click_show_hide_password()
        expected_result = recovery_password_page.get_attribute_field(RecoveryPageLocator.ACTIVE_FIELD_PASSWORD, 'class')
        assert 'input_status_active' in expected_result


