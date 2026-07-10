import requests

class ProjectsAPI:
    def __init__(self, url, login, password) -> None:
        self.url = url
        self.login = login
        self.password = password

    
    def get_keys_list(self):
        body = {
            "login": self.login,
            "password": self.password,
        }
        resp = requests.post(self.url + '/api-v2/auth/keys/get', json=body)
        resp.raise_for_status()
        data = resp.json()
        

    def positive_create_project(self, title):
        my_token = self.get_keys_list() 
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}"
        }
        project = {"title": title}
        
        resp = requests.post(
            self.url + '/api-v2/projects', 
            json=project, 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()["id"]
    
    def negative_create_project(self, title):
        my_token = self.get_keys_list() 
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}"
        }
        project = {"title": title}
        
        resp = requests.put(
            self.url + '/api-v2/projects', 
            json=project, 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()["id"]

    def positive_update_project(self, project_id, new_title):
        my_token = self.get_keys_list()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}"
        }
        new_project = {"title": new_title}
        
        resp = requests.put(
            self.url + f'/api-v2/projects/{project_id}', 
            json=new_project, 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()["id"]
    
    def negative_update_project(self, project_id, new_title):
        my_token = self.get_keys_list()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}"
        }
        new_project = {"title": new_title}
        
        resp = requests.put(
            self.http + f'/api-v2/projects/{project_id}', 
            json=new_project, 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()["id"]

    def positive_get_project_id(self, project_id):
        my_token = self.get_keys_list()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}"
        }
        
        resp = requests.get(
            self.url + f'/api-v2/projects/{project_id}', 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()
    
    def negative_get_project_id(self, project_id):
        my_token = self.get_keys_list()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}"
        }
        
        resp = requests.get(
            self.url + f'/api-v2/project/{project_id}', 
            headers=my_headers
        )
        resp.raise_for_status()
        return resp.json()


