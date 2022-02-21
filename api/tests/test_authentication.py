from rest_framework import status
import pytest


class TestAuthentication:

    def test_unauthorized_request(self, get_client):
        url = '/api/products/'
        response = get_client.get(url)
        assert response.status_code == 401

    # def test_authorized_request(self, get_client, get_token):
    #     url = '/api/products'
    #     get_client.credentials(HTTP_AUTHORIZATION='Token ' + get_token)
    #     response = get_client.get(url)
    #     assert response.status_code == 200

    # def test_create_product_with_bad_token(self, get_client):
    #     get_client.credentials(HTTP_AUTHORIZATION='Bearer ' + "bad token")
    #     response = get_client.post(
    #         "/api/products/", {
    #             "name": "botella de plastico",
    #             "price": 360,
    #             "stock": 6
    #         },
    #         format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
