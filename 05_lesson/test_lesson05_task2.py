from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()
    sleep(2)

    driver.find_element(By.NAME, "custname").send_keys("Sergey")
    sleep(2)
    driver.find_element(
        By.XPATH, "//button[normalize-space()='Submit order']").click()
    assert driver.current_url
    sleep(2)

    driver.quit()
