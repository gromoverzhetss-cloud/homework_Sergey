
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in fields.items():
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.send_keys(value)

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".alert-danger")))

    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_field.get_attribute(
        "class"), \
        f"Ожидался класс 'alert-danger' у zip-code, получили: '{
            zip_code_field.get_attribute('class')}'"
    valid_fields = [
        (By.CSS_SELECTOR, "#first-name"),
        (By.CSS_SELECTOR, "#last-name"),
        (By.CSS_SELECTOR, "#address"),
        (By.CSS_SELECTOR, "#e-mail"),
        (By.CSS_SELECTOR, "#phone"),
        (By.CSS_SELECTOR, "#city"),
        (By.CSS_SELECTOR, "#country"),
        (By.CSS_SELECTOR, "#job-position"),
        (By.CSS_SELECTOR, "#company"),
    ]

    for alert in valid_fields:
        field = driver.find_element(*alert)
        assert "alert-success" in field.get_attribute("class"), \
            f"Поле {alert("alert-danger")}: \
ожидался класс 'alert-success', получили '{
            field.get_attribute('class')}'"

    driver.quit()
