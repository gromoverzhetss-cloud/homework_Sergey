import faker
import config
from pages.profile_page import ProfilePage



fake = faker.Faker()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f"{first_name} {last_name}"


def test_change_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page("dragobor")
    profile.update_profile(first_name, last_name)
    profile.open_profile_page("dragobor")

    assert profile.get_user_name() == full_name, "Имя профиля не было обновлено"

def test_check_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page("dragobor")
    name = profile.get_user_name()

    assert name != "", "Имя профиля должно быть не пустым"
    assert len(name) > 0, "Имя профиля содержит хотя бы один символ"