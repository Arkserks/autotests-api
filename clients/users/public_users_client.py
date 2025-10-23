from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с  /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание нового пользователя
        :param request: Словарь с email, password, lastName, firstName, middleName
        :return: Объект Response с данными ответа.
        """
        return self.client.post("/api/v1/users", json=request)