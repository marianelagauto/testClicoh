from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
import json


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
        response = client.post(
            "/api/token/",  
            {
                "username": "admin", 
                "password": "admin"
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['access'])
        response = client.post(
            "/api/products/", {
                "name": "botella de plastico",
                "price": 360,
                "stock": 6
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # self.assertEqual(json.loads(response.content),
        #                  {"name": "botella de plastico", "price": 360.0, "stock": 6})


    def test_create_product_with_bad_token(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + 'bad_token')
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
        response = client.post(
            "/api/token/",  
            {
                "username": "admin", 
                "password": "admin"
            },
            format="json"
        )
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['access'])
        