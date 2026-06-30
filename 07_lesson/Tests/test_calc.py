import pytest
from selenium import webdriver
from page.page_calc import CalculatorPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    

def test_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    page_calc = CalculatorPage(driver, url)
    page_calc.open()
    page_calc.set_delay()
    page_calc.enter_expression()
    page_calc.get_result()
    assert page_calc.get_result() == "15"