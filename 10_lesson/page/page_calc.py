import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CalculatorPage:
    """Класс страницы калькулятора для автоматизации тестирования."""

    DELAY_INPUT = (By.CSS_SELECTOR, '#delay')
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 45)
         """
        Инициализирует страницу калькулятора.

        param driver: Экземпляр драйвера Selenium для управления браузером.
        type driver: selenium.webdriver.remote.webdriver.WebDriver
        param url: URL-адрес страницы калькулятора.
        type url: str
        """

    
    def open(self):
        with allure.step("Открыть сайт компании"):
            self.driver.get(self.url)
           
    
    def set_delay(self):
        with allure.step("Найти поле задержки delay"):
            delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        with allure.step("Нажать на поле задержки delay"):
            delay_input.clear()
        with allure.step("Ввести в поле цифру 45"):
            delay_input.send_keys("45")

    
    def enter_expression(self):
            with allure.step("Найти кнопки 7, +, 8, = и нажать"):
                buttons = ["7", "+", "8", "="]
                for button in buttons:
                    xpath = f"//span[text()='{button}']"
                    self.driver.find_element(By.XPATH, xpath).click()

   
    def get_result(self):
        with allure.step("Проверить что в окне отобразится результат 15 через 45 секунд"):
            self.wait.until(EC.text_to_be_present_in_element(self.RESULT_SCREEN, "15"))
            result_element = self.driver.find_element(*self.RESULT_SCREEN)
            return result_element.text
            """
            Получает результат вычисления из экрана калькулятора.
    
            return: Текстовое значение результата вычисления.
            """
