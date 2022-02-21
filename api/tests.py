from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
import json


def get_token():
    client = APIClient()
    response = client.post(
        "/api/token/",
        {
            "username": "admin",
            "password": "admin"
        },
        format="json"
    )
    return response.data['access']


class AuthenticationTestCase(TestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'myemail@test.com', 'admin')
        return super().setUp()

    def test_create_product_without_authentication(self):
        client = APIClient()
        response = client.post(
            "/api/products/", {
                "name": "botella de plastico",
                "price": 360,
                "stock": 6
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_product_with_authentication(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_token())
        response = client.post(
            "/api/products/", {
                "name": "producto 1",
                "price": 360,
                "stock": 6
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),
                         {"id": 1, "name": "producto 1", "price": 360.0, "stock": 6})

    def test_create_product_with_bad_token(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'bad_token')
        response = client.post(
            "/api/products/", {
                "name": "botella de plastico",
                "price": 360,
                "stock": 6
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class OrderTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'myemail@test.com', 'admin')
        return super().setUp()

    def test_create_order_detail(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_token())
        response = client.post(
            '/api/orders/', {
                "date_time": "2022-02-15 01:23:00",
                "details": [
                    {
                        "product": 3,
                        "cuantity": 8
                    },
                    {
                        "product": 3,
                        "cuantity": 1
                    }
                ]
            }
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
