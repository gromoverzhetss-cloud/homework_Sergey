from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    driver.maximize_window()
    sleep(20)

    driver.find_element(By.LINK_TEXT, "HTML form").click()
    sleep(2)
    assert driver.current_url == "https://httpbin.org/forms/post"
    driver.back()

    assert driver.current_url == "https://httpbin.org/"
    sleep(2)
    driver.quit()
