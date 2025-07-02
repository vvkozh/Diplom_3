from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать изменения текста в элементе')
    def wait_change_element(self, locator, element_text, timeout=10):
        return WebDriverWait(self.driver, timeout).until((lambda d: ((element := d.find_element(*locator)) and element.text != element_text and element.text)))

    @allure.step('Подождать загрузку всех элементов по локатору')
    def wait_load_all_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельности элемента')
    def wait_clickable_element(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Подождать скрытия элемента')
    def wait_hide_element(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout = 10):
        element = self.wait_clickable_element(locator, timeout)
        element.click()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ввод текста в поле')
    def send_text_to_input(self, locator, text, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Получить атрибут элемента')
    def get_attribute_on_element(self, locator, attribute, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)

    @allure.step('Получить URL страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Переход по ссылке')
    def going_url(self, url):
        self.driver.get(url)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element