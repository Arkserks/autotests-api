import httpx

login_payload = {
    "email": "aleks@example.com",
    "password": "first"
}

with httpx.Client() as client:
    login_response = client.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
    print("Код ответа post_login:", login_response.status_code, "\n---")
    print("JSON ответа post_login:", "\n", login_response.json(), "\n---")
    login_token = login_response.json()['token']['accessToken']
    # print(login_token)

    headers = {
    "Authorization": f"Bearer {login_token}"
    }
    get_me_response = client.get("http://localhost:8000/api/v1/users/me", headers=headers)
    print("Код ответа get_me:", get_me_response.status_code, "\n---")
    print("JSON ответа get_me:", "\n", get_me_response.json(), "\n---")
