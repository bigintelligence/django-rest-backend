from rest_framework.test import APITestCase
from rest_framework import status


URL_TEST_BASE = '/api/inmuebles/'


class TestInmuebles(APITestCase):
    def test_list_all(self):
        response = self.client.get(URL_TEST_BASE, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
