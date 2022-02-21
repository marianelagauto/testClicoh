# conftest.py
import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture(scope="session", autouse=True)
def get_client():
    return APIClient()

@pytest.fixture(scope="session", autouse=True)
def create_user():
	return User.objects.create_superuser('admin', 'myemail@test.com', 'admin')

@pytest.fixture(scope="session", autouse=True)
def get_token():
   response = APIClient().post(
        "/api/token/",
        {
            "username": "admin",
            "password": "admin"
        },
        format="json"
    )
   return response.data['access']

@pytest.fixture(scope="session", autouse=True)
def product_data():
   return {"name":"producto 1", "price":360, "stock":5}