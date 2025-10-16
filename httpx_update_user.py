import httpx
from tools.fakers import get_random_email

# Данные для авторизации
login_payload = {
    "email": "aleks@example.com",
    "password": "first"
}

with httpx.Client() as client:
    # Аутентификация и получение токена
    login_response = client.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
    print("Код ответа post_login:", login_response.status_code, "\n---")
    print("JSON ответа post_login:", "\n", login_response.json(), "\n---")
    login_token = login_response.json()['token']['accessToken']
    # print(login_token)

    # Данные для создания юзера
    create_user_payload = {
        "email": get_random_email(),
        "password": "string",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
    # Создание юзера
    create_user_response = client.post("http://localhost:8000/api/v1/users", json=create_user_payload)
    print("Код ответа create_user:", create_user_response.status_code, "\n---")
    print("JSON ответа create_user:", "\n", create_user_response.json(), "\n---")

    headers = {
        "Authorization": f"Bearer {login_token}"
    }

    # Данные для обновления юзера
    update_user_payload = {
        "email": get_random_email(),
        "lastName": "string1",
        "firstName": "string2",
        "middleName": "string3"
    }

    # Обновление данных юзера
    update_user_response = client.patch(f"http://localhost:8000/api/v1/users/{create_user_response.json()['user']['id']}", headers=headers, json=update_user_payload)
    print("Код ответа update_user:", update_user_response.status_code, "\n---")
    print("JSON ответа update_user:", "\n", update_user_response.json(), "\n---")