from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwagLabs:
    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN = (By.CSS_SELECTOR,"#login-button")
    BACKPACK = (By.NAME, "add-to-cart-sauce-labs-backpack")
    SHIRT = (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.NAME, "add-to-cart-sauce-labs-onesie")


    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    def open(self):
            self.driver.get("https://www.saucedemo.com/cart.html")

    def authorization(self):
        name = self.wait.until(EC.presence_of_element_located(
            self.USERNAME
        ))
        name.send_keys("standard_user")

        password = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD
        ))
        password.send_keys("secret_sauce")

        login_button = self.wait.until(EC.presence_of_element_located(
            self.LOGIN
        ))
        login_button.click()
    def products(self):
        self.wait.until(
          EC.presence_of_element_located(self.BACKPACK)
        ).click()
        self.wait.until(
            EC.presence_of_element_located(self.SHIRT)
        ).click()
        self.wait.until(
        EC.presence_of_element_located(self.ONESIE)
        ).click()

class Your_Cart:
    BASKET = (By.CSS_SELECTOR, ".shopping_cart_link")
    CHEKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    def basket(self):
         self.wait.until(
            EC.presence_of_element_located(self.BASKET)
         ).click()
    def chekout(self):
         self.wait.until(
              EC.presence_of_element_located(self.CHEKOUT_BUTTON)
         ).click()
    def form_completion(self):
         first_name = self.wait.until(
              EC.presence_of_element_located(self.FIRST_NAME)
         )
         first_name.send_keys("Иван")

         last_name = self.wait.until(
              EC.presence_of_element_located(self.LAST_NAME))
         last_name.send_keys("Петров")

         postal_code = self.wait.until(
              EC.presence_of_element_located(self.POSTAL_CODE))
         postal_code.send_keys("144006")

    def continue_button(self):
          self.wait.until(
               EC.presence_of_element_located(self.CONTINUE_BUTTON)
          ).click()

    def total_label(self):
             self.wait.until(
                   EC.presence_of_element_located(self.TOTAL))
             
    def total_result(self):
         self.wait.until(EC.text_to_be_present_in_element(
              self.TOTAL, "Total: $58.29"))
         result_total_label = self.driver.find_element(*self.TOTAL)
         return result_total_label.text
         