import requests

class CompanyApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_company_list(self, params_to_add=None):
        """
        Получает список компаний через API.
        params_to_add - дополнительные параметры для фильтрации (например, активные компании)
        """
        url = f"{self.base_url}/companies"
        response = requests.get(url, params=params_to_add)
        # Проверяем, что запрос прошел успешно
        response.raise_for_status()
        # Возвращаем данные в виде списка словарей
        return response.json()
    def set_active_state(self, id, is_active):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/status_update/{id}?client_token={client_token}"
        resp = requests.patch(url_with_token,
                              json={"is_active": is_active})
        return resp.json()
    