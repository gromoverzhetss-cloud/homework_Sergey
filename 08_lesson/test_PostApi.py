from PostApi import ProjectsAPI
from dotenv import load_dotenv
import os
import time  
import pytest

load_dotenv()

api_url = os.getenv("API_URL")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
id = os.getenv("ID")


api = ProjectsAPI(api_url, login, password)

@pytest.mark.positive_test
def test_positive_create_project():
    title = f"Times {int(time.time())}"
    project_id = api.positive_create_project(title)  
    assert project_id.status_code == 200
    project = api.get_project_id(project_id)
    assert project["title"] == title

@pytest.mark.negative_test
def test_negative_create_project():
    title = f"Times {int(time.time())}"
    project_id = api.negative_create_project(title)  
    assert project_id.status_code == 404
    project = api.get_project_id(project_id)
    assert project["title"] == title


@pytest.mark.positive_test
def test_positive_update_project():
    original_title = f"{int(time.time())}"
    project_id = api.positive_create_project(original_title)
    assert updated_id.status_code == 200
    new_title = "New progect"
    updated_id = api.positive_update_project(project_id, new_title)

@pytest.mark.negative_test
def test_negative_update_project():
    original_title = f"{int(time.time())}"
    project_id = api.positive_create_project(original_title)
    assert updated_id.status_code == 404
    new_title = "New progect"
    updated_id = api.negative_update_project(project_id, new_title)  
    
    assert updated_id == project_id

@pytest.mark.positive_test
def test_positive_get_progect_id():
    login = os.getenv("login")
    password = os.getenv("password")
    api.get_keys_list(login, password)
    found_project = api.positive_get_project_id(id)
    assert found_project.status_code == 200
    assert found_project 

@pytest.mark.negative_test
def test_negative_get_progect_id():
    login = os.getenv("login")
    password = os.getenv("password")
    api.get_keys_list(login, password)
    found_project = api.negative_get_project_id(id)
    assert found_project.status_code == 404
    assert found_project   
    




