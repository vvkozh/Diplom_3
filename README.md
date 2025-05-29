## Дипломный проект часть 3
<hr>

## Студент: Владимир Кожевников

## <h>Когорта: #18_FS</h>
<hr>

## Автоматизация тестирования сайта "Stellar Burgers"

### Этот проект содержит автотесты для сайта "Stellar Burgers" (https://stellarburgers.nomoreparties.site/), написанные с использованием **Selenium WebDriver**, **Pytest** и паттерна **Page Object Model (POM)**.
### Тесты проверяют:
### • восстановление пароля;
### • различные переходы в личном кабинете;
### • основные функциональности на главной странице;
### • раздел "Лента заказов".

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=allure_results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results

<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла            | Содержание файла                              |
|---------------------------|-----------------------------------------------|
| tests.dir                 | Директория с тестами                          |
| test_check_basic_funk.py  | Тесты на проверку базового функционала        |
| test_order_feed.py        | Тесты на проверку ленты заказов               |
| test_personal_account.py  | Тесты на проверку переходов в личном кабинете |
| test_recovery_password.py | Тесты на восстановление пароля                |
| locators.dir              | Директория с локаторами                       |
| pages dir                 | Директория с методами на страницах            |
| conftest.py               | Фикстуры                                      |
| curls.py                  | Файл с URL                                    |
| data.py                   | Файл с URL и body запросов                    |
| curls.py                  | Файл с вспомогательными методами              |
| requirements.txt          | Файл с зависимостями                          |
| allure_results.dir        | Папка с отчетами Allure                       |
