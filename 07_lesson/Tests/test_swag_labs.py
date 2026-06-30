import pytest
from selenium import webdriver
from page.swag_labs_page import SwagLabs
from page.swag_labs_page import Your_Cart


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_shop(driver):
    shop = SwagLabs(driver, "https://www.saucedemo.com/")
    shop.open()
    shop.authorization()
    shop.products()
    shop = Your_Cart(driver, "https://www.saucedemo.com/cart.html")
    shop.basket()
    shop.chekout()
    shop.form_completion()
    shop.continue_button()
    shop.total_label()
    shop.total_result()
    assert shop.total_result() == "Total: $58.29"