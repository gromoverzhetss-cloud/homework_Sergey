from selenium.webdriver.common.by import By

class ProjectsPage:
    # Локаторы элементов
    NEW_PROJECT_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-success")
    PROJECT_TITLE_INPUT = (By.ID, "projectTitle")
    CREATE_BUTTON = (By.CSS_SELECTOR, "button.btn-success[type='submit']")
    PROJECT_CARDS = (By.CLASS_NAME, "gf-project-card")
    PROJECT_TITLE_IN_CARD = (By.CSS_SELECTOR, "h6.mb-0 a")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://gitflic.ru/project/"

    def open(self):
        self.driver.get(self.url)

    def click_new_project(self):
        self.driver.find_element(*self.NEW_PROJECT_BUTTON).click()

    def create_project(self, project_name):
        # Заполняем название
        title_field = self.driver.find_element(*self.PROJECT_TITLE_INPUT)
        title_field.clear()
        title_field.send_keys(project_name)

        # Скроллим и нажимаем создать
        create_btn = self.driver.find_element(*self.CREATE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", create_btn)
        create_btn.click()

    def get_project_names(self):
        # Получаем все карточки проектов
        cards = self.driver.find_elements(*self.PROJECT_CARDS)
        names = []

        for card in cards:
            try:
                # Ищем название внутри карточки
                title_element = card.find_element(*self.PROJECT_TITLE_IN_CARD)
                names.append(title_element.text)
            except:
                continue

        return names