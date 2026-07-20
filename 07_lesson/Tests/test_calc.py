import allure
import pytest
from selenium import webdriver
from page.page_calc import CalculatorPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    """
    Фикстура для создания и управления экземпляром драйвера Chrome.

    Создаёт экземпляр Chrome, разворачивает окно на весь экран,
    предоставляет драйвер для теста, затем корректно закрывает браузер.
    """

@allure.feature("Тестирование калькулятора")
@allure.severity("critical")
@allure.title("Тестирование калькулятора")   
@allure.epic("КАЛЬКУЛЯТОР")
@allure.description("Открытие сайта компании через переменную url")
def test_calculator(driver):
    """
    Тест проверки работы калькулятора с задержкой.
"""
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    page_calc = CalculatorPage(driver, url)
    """Инициализировать страницу калькулятора"""
    page_calc.open()
    """Открыть страницу"""
    page_calc.set_delay()
    """Установить задержку (ввести 45)"""
    page_calc.enter_expression()
    """Ввести выражение '7 + 8 ='"""
    page_calc.get_result()
    """Получить и проверить результат вычисления"""
    assert page_calc.get_result() == "15"
