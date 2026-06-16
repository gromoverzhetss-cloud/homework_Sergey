from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.CSS_SELECTOR, "button").click()

    message = wait.until(
        EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
    )
    driver.save_screenshot("screenshots/Hello_world.png")
    message = driver.find_element(By.ID, "finish")
    assert message.text == "Hello World!"

    driver.quit()
