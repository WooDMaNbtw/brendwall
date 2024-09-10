from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product


class ProductAPITestCase(APITestCase):

    def setUp(self):
        self.valid_payload = {
            'title': 'Valid Product',
            'description': 'This is a valid product',
            'price': 50.00
        }
        self.invalid_payload_no_title = {
            'title': '',
            'description': 'No title',
            'price': 100.00
        }
        self.invalid_payload_negative_price = {
            'title': 'Invalid Product',
            'description': 'This product has a negative price',
            'price': -50.00
        }

    def test_create_valid_product(self):
        """ Successful product creation """
        response = self.client.post(reverse('products'), self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, 'Valid Product')

    def test_create_product_no_title(self):
        """ Unsuccessful product creation due to empty title """
        response = self.client.post(reverse('products'), self.invalid_payload_no_title, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Title is required.', response.data['detail'])

    def test_create_product_negative_price(self):
        """ Unsuccessful product creation due to negative price """
        response = self.client.post(reverse('products'), self.invalid_payload_negative_price, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Price cannot be negative.', response.data['detail'])

