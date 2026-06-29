from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "NWYzZGJiYTUtMmZkNi00YTQzLWE5MTYtMDg4MjZjMGFkNDNh",
        "domain": "gitflic.ru"
        })

    driver.add_cookie({
       "name": "cookiesAccepted",
       "value": "true",
       "domain": "gitflic.ru"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/dragobor")
    user_1 = driver.current_url
    driver.delete_all_cookies()
    driver.refresh()

    driver.add_cookie({
        "name": "SESSION",
        "value": "ZDg4NWMyMTMtMzAxNS00N2YyLTkyNjktNDEwYzdjZDUzOTUy",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/chimihumu")
    wait.until
    user_2 = driver.current_url
    assert user_1 != user_2

    driver.quit()
