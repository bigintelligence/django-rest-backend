from rest_framework.test import APITestCase
from rest_framework import status


URL_BASE = '/api/'
URL_INMUEBLES = 'inmuebles/'
URL_CARGA = 'carga/'


class TestInmuebles(APITestCase):
    """Testing the endpoints on Inmueblesapi app"""
    def test_carga(self):
        response = self.client.get(URL_BASE+URL_CARGA, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all(self):
        response = self.client.get(URL_BASE+URL_INMUEBLES, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
