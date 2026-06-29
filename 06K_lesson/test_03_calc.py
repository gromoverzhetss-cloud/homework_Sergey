from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("http://www.saucedemo.com/")
    user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(
        (By.NAME, 'add-to-cart-sauce-labs-backpack')))
    backpack = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
    backpack.click()
    shirt = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    shirt.click()
    onesie = driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie")
    onesie.click()

    basket = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    basket.click()

    checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout_button.click()
    WebDriverWait(driver, 10)
    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Ivan")

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Petrov")

    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("144006")

    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_button.click()

    total = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
    total_text = total.text
    print(f"Получена итоговая стоимость: {total_text}")

    total_sum = "Total: $58.29"
    assert total_text == total_sum
    driver.quit()
