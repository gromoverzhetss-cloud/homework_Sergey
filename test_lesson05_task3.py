
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    driver.maximize_window()

    elements = driver.find_elements(By.TAG_NAME, 'a')
    print(f"Найдено: {len(elements)}")
    if elements == 10:
        print("ok")
    else:
        print("no")

    for element in elements:
        assert element.is_displayed()
    if elements[0] == 1:
        print(True)
    else:
        print(False)
    driver.quit()
