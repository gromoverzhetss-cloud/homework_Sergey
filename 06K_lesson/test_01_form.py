from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    button_submit = driver.find_element(By.CSS_SELECTOR, "button")
    button_submit.click()

    zip_code = driver.find_element(By.ID, "zip-code")
    color_zip_code = zip_code.value_of_css_property("background-color")
    assert color_zip_code == "rgba(248, 215, 218, 1)"
    color_green = [(By.NAME, "first-name"),
                   (By.NAME, "last-name"),
                   (By.NAME, "address"),
                   (By.NAME, "e-mail"),
                   (By.NAME, "phone"),
                   (By.NAME, "city"),
                   (By.NAME, "country"),
                   (By.NAME, "job-position"),
                   (By.NAME, "company")
                   ]
    for field_id in color_green:
        field_element = wait.until(EC.visibility_of_element_located(
            (By.ID, field_id)))
        background_color = field_element.value_of_css_property
        ("background-color")
    assert background_color == "rgb(209, 231, 221)"

    driver.quit()
