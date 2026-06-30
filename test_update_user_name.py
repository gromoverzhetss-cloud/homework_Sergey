import faker
from playwright.sync_api import Page


def test_update_user_name(main_page):
    # Перейти на страницу профиля
    main_page.goto("https://gitflic.ru/user/dragobor")
    main_page.screenshot(path="screenshots/full_page.png")
    # Нажать кнопку редактирования профиля
    main_page.locator("user-profile__edit").click()

# Изменить Ф и И в форме
    user_name = faker.Faker().user_name()
    main_page.locator("#name").fill(user_name)

    user_surname = faker.Faker().last_name()
    main_page.locator("#surname").fill(user_surname)

# Сохранить изменения
    main_page.locator(".gf-button.--success").click

# Вернуться на страницу профиля
    main_page.doto("https://gitflic.ru/user/dragobor")
    main_page.screenshot(path="screenshots/full_page.png")

# Ожидаемый результат: Ф и И успешно изменены и отображается на странице профил
    user_name_main = main_page.locator("h6.mb-0")
    user_name_main.screenshot(path="screenshots/full_page.png")

    Page(user_name_main).to_have_text(user_name+" "+user_surname)
