from pages.projects_page import ProjectsPage
import faker


def test_create_and_check_project(driver_authorized):
    # Создаём страницу проектов
    projects_page = ProjectsPage(driver_authorized)

    # Открываем страницу
    projects_page.open()

    # Генерируем имя для проекта
    fake = faker.Faker()
    project_name = f"Мой проект {fake.word()}"

    # Создаём проект
    projects_page.click_new_project()
    projects_page.create_project(project_name)

    # Возвращаемся на страницу проектов
    projects_page.open()

    # Получаем список проектов
    all_projects = projects_page.get_project_names()

    # Ищем созданный проект в списке
    project_found = False
    for project in all_projects:
        if project_name in project:
            project_found = True
            break

    # Проверяем
    assert project_found, f"Проект '{project_name}' не найден в списке"