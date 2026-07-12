import requests
from urllib.parse import urljoin

class ProjectsAPI:
    def __init__(self, url, login, password, api_key) -> None:
        self.url = url.rstrip("/")
        self.login = login
        self.password = password
        self.api_key = api_key  

    def _make_url(self, endpoint):
        return urljoin(self.url, endpoint)

    def get_keys_list(self):
        body = {
            "login": self.login,
            "password": self.password,
        }
        resp = requests.post(self._make_url('/api-v2/auth/keys/get'), json=body)
        resp.raise_for_status()
        return resp.json()

    def positive_create_project(self, title):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"  
        }
        project = {"title": title}
        
        resp = requests.post(
            self._make_url('/api-v2/projects'), 
            json=project, 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()["id"]
    
    def positive_update_project(self, project_id, new_title):
        
        my_token = self.api_key 
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}"
        }
        new_project = {"title": new_title}
        
        resp = requests.put(
            self._make_url(f'/api-v2/projects/{project_id}'), 
            json=new_project, 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()["id"]
    
    def positive_get_project_id(self, project_id):
        
        my_token = self.api_key
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}"
        }
        
        resp = requests.get(
            self._make_url(f'/api-v2/projects/{project_id}'), 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()  
    def create_project_raw(self, title):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        project = {"title": title}
        
        resp = requests.post(
            self._make_url('/api-v2/projects'), 
            json=project, 
            headers=my_headers
        )
        return resp 

    def update_project_raw(self, project_id, new_title):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {"title": new_title}
        
        resp = requests.put(
            self._make_url(f'/api-v2/projects/{project_id}'), 
            json=payload, 
            headers=my_headers
        )
        return resp

    def get_project_raw(self, project_id):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        resp = requests.get(
            self._make_url(f'/api-v2/projects/{project_id}'), 
            headers=my_headers
        )
        return resp

