import os
import requests
from dotenv import load_dotenv

load_dotenv(r"C:\Users\Елена\Desktop\Python\lesson_08\YouGileKeys.env")


class YouGileApi:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")

    def get_token(self):
        login = os.getenv("YOUGILE_LOGIN")
        password = os.getenv("YOUGILE_PASSWORD")
        company_id = os.getenv("YOUGILE_COMPANY_ID")

        if not login or not password or not company_id:
            raise ValueError("Не заполнены YOUGILE_LOGIN, YOUGILE_PASSWORD или YOUGILE_COMPANY_ID")

        response = requests.post(
            f"{self.base_url}/auth/keys",
            json={
                "login": login,
                "password": password,
                "companyId": company_id,
            },
        )

        print("STATUS:", response.status_code)
        print("TEXT:", response.text)

        response.raise_for_status()
        return response.json()["key"]

    def create_project(self, token, title):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.post(f"{self.base_url}/projects", json={"title": title}, headers=headers)

    def get_project(self, token, project_id):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.get(f"{self.base_url}/projects/{project_id}", headers=headers)

    def update_project(self, token, project_id, **data):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.put(f"{self.base_url}/projects/{project_id}", json=data, headers=headers)

    def delete_project(self, token, project_id):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.delete(f"{self.base_url}/projects/{project_id}", headers=headers)
