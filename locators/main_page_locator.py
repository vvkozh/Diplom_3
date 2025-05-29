from selenium.webdriver.common.by import By

class MainPageLocator:
    OVERLAY = (By.XPATH, '//div[@class="Modal_modal__P3_V5"]/div[@class="Modal_modal_overlay__x2ZCr"]')
    BUT_PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]')
    TEXT_COLLECT_BURGER = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')
    TEXT_FEED_ORDER = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')
    BUT_CONSTRUCTOR = (By.XPATH, '//a[@href="/"]/descendant::p[contains(text(), "Конструктор")]')
    BUT_FEED_ORDER = (By.XPATH, '//a[@href="/feed"]')
    HEAD_INGREDIENT_DETAIL = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    BUT_CROSS = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    BURGER_CONSTRUCTOR = (By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket__list__l9dp_")]')
    BUT_CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    TEXT_ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')
    INGREDIENT_LOCATOR = {'buns': [['bun_1', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')],
                                   ['bun_2', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')]],

                          'souses': [['souses_1', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')],
                                     ['souses_2', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]')],
                                     ['souses_3', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa74"]')],
                                     ['souses_4', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa75"]')]],

                          'toppings': [['topping_1', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]')],
                                       ['topping_2', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]')],
                                       ['topping_3', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa71"]')],
                                       ['topping_4', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]')],
                                       ['topping_5', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa76"]')],
                                       ['topping_6', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa77"]')],
                                       ['topping_7', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa78"]')],
                                       ['topping_8', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa79"]')],
                                       ['topping_9', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa7a"]')]]
                          }