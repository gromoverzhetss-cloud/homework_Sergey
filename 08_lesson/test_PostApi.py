import time
import pytest
from dotenv import load_dotenv
import os
from PostApi import ProjectsAPI 

load_dotenv()

@pytest.fixture
def api():
  
    url = os.getenv("API_URL")
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    api_key = os.getenv("KEY")
    
        
    return ProjectsAPI(url, login, password, api_key)

@pytest.fixture
def created_project_id(api):

    title = f"Test Project {int(time.time())}"
    pid = api.positive_create_project(title)
    yield pid
  



def test_positive_create_project(api):
    title = f"Times {int(time.time())}"
    project_id = api.positive_create_project(title)
    assert project_id is not None
    
    project = api.positive_get_project_id(project_id)
    assert project["title"] == title
    

def test_positive_update_project(created_project_id, api):
    new_title = "Updated Title"
    updated_id = api.positive_update_project(created_project_id, new_title)
    
    
    assert updated_id == created_project_id
    
   
    project = api.positive_get_project_id(created_project_id)
    assert project["title"] == new_title

def test_positive_get_project_by_id(created_project_id, api):
    project = api.positive_get_project_id(created_project_id)
    assert project is not None
    assert "title" in project



def test_negative_create_project_empty_title(api_client):

    resp = api_client.create_project_raw("")
    

    assert resp.status_code in [400, 404], f"Ожидался 400/422, получен {resp.status_code}"
    
    data = resp.json()
  
    assert "errors" in data or "message" in data

def test_negative_update_nonexistent_project(api_client):
    fake_id = 999999
    new_title = "New Title"
    
    resp = api_client.update_project_raw(fake_id, new_title)
    

    assert resp.status_code == 404, f"Ожидался 404, получен {resp.status_code}"

def test_negative_get_nonexistent_project(api_client):
    fake_id = 999999
    
    resp = api_client.get_project_raw(fake_id)
    
    assert resp.status_code == 404

    




