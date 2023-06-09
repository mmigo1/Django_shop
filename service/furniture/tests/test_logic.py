from rest_framework.test import APITestCase
from django.urls import reverse
from django.test import TestCase
from furniture.serializer import FurnitureSerializer
from furniture.models import Furniture
from rest_framework import status


class FurnApiTestCase(APITestCase):
    def test_get_list(self):
        furn_1 = Furniture.objects.create(name='Табурет эконом', price=450)
        furn_2 = Furniture.objects.create(name='Диван эконом', price=1450)

        response = self.client.get(reverse('furn_api_list'))

        serial_data = FurnitureSerializer([furn_2, furn_1], many=True).data
        serial_data = {'furn_list': serial_data}

        self.assertEqual(serial_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post_list(self):
        data = {'name': 'Диван эконом', 'price': 1450, 'description': '', 'exist': True}
        response = self.client.post(reverse('furn_api_list'), data=data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


class FurnApiDetailTestCase(APITestCase):
    def test_get_detail(self):
        furn_3 = Furniture.objects.create(name='Табурет эконом', description='', price=450, exist='True')
        response = self.client.get(reverse('furn_api_detail', kwargs={'pk': 3}))

        self.assertEqual(response.data, {'name': 'Табурет эконом', 'description': '', 'price': 450.0, 'exist': True})
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_put_detail(self):
        furn_4 = Furniture.objects.create(name='Табурет эконом', price=450, description='', exist=True, )
        data = {'name': 'Диван эконом'}
        response = self.client.put(reverse('furn_api_detail', kwargs={'pk': 4}), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


    def test_delete_detail(self):
        furn_1 = Furniture.objects.create(name='Табурет эконом', price=450)
        furn_2 = Furniture.objects.create(name='Диван эконом', price=1450)
        response = self.client.delete(reverse('furn_api_detail', kwargs={'pk': 2}))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        response = self.client.get(reverse('furn_api_detail', kwargs={'pk': 2}))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        response = self.client.get(reverse('furn_api_detail', kwargs={'pk': 1}))
        self.assertEqual(response.data['name'], furn_1.name)
