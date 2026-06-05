
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()

    driver.find_element(By.NAME, "custname").send_keys("Sergey")
    driver.find_element(
        By.XPATH, "//button[normalize-space()='Submit order']").click()
    assert driver.current_url
   

    driver.quit()
