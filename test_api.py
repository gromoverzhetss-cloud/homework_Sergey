from PostApi import ProjectsAPI
from dotenv import load_dotenv
import os
import time  

load_dotenv()

api_url = os.getenv("API_URL")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


api = ProjectsAPI(api_url, login, password)


def test_get_keys():
    result = api.get_keys_list()
    assert result, "Токен не получен"
    assert isinstance(result, str), "Токен должен быть строкой"


def test_create_project():

    title = f"Times {int(time.time())}"
    project_id = api.create_project(title)  
    assert project_id is not None, "ID  не получен"
    assert project_id.status_code == 200
    project = api.get_project_id(project_id)
    assert project["title"] == title


def test_update_project():
    original_title = f"{int(time.time())}"
    project_id = api.create_project(original_title)
    
    new_title = "New progect"
    updated_id = api.update_project(project_id, new_title)  
    
    assert updated_id == project_id
    
    project = api.get_project_id(project_id)
    assert project["title"] == new_title
