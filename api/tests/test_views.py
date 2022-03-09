from .base_tests import TestData
from django.urls import reverse
from rest_framework import status
from api.models import Sensor, Metrics
from api.serializers import SensorSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class SensorListTest(TestData):
    def test_get_all_sensors(self):
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        url = reverse('sensor_list')
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request(self):
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        url = reverse('sensor_list')
        response = client.post(url, {'name': 'Sensor3', 'room': 'Living Room', 'board': 'Esp32'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_sensor_bad_request(self):
        '''
        Violate unique name field constraint
        '''
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        url = reverse('sensor_list')
        response = client.post(url, {'name': 'Sensor1', 'room': 'Different Room', 'board': 'Esp32'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class SensorDetailTest(TestData):
    def test_valid_get_sensor(self):
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        pk = self.sensor1.id
        url = reverse('sensor_detail', kwargs={'pk': pk})
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorSerializer(sensor, many=True)
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_sensor(self):
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        pk = '6f41df41-9eea-44cd-ac1e-2f4d22c3ac03' # some random uuid
        url = reverse('sensor_detail', kwargs={'pk': pk})
        sensor = Sensor()
        # Test raised exception
        with self.assertRaises(sensor.DoesNotExist):
            sensor = Sensor.objects.get(pk=pk)
        serializer = SensorSerializer(sensor, many=True)
        response = client.get(url, format='json')
        # Test response code
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_put_request(self):
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        pk = self.sensor1.id
        url = reverse('sensor_detail', kwargs={'pk': pk})
        response = client.put(url, {'name': 'New Sensor', 'room': 'New Room', 'board': 'Esp8266'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_put_request(self):
        '''
        Board field is not provided, so the response should be 400
        '''
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        pk = self.sensor1.id
        url = reverse('sensor_detail', kwargs={'pk': pk})
        response = client.put(url, {'name': 'New Sensor', 'room': 'New Room'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_request_not_existing_sensor(self):
        pk = '6f41df41-9eea-44cd-ac1e-2f4d22c3ac08' # some random uuid
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        url = reverse('sensor_detail', kwargs={'pk': pk})
        response = client.put(url, {'name': 'New Sensor', 'room': 'New Room'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_valid_sensor(self):
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        pk = self.sensor1.id
        url = reverse('sensor_detail', kwargs={'pk': pk})
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_not_existing_sensor(self):
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        pk = '6f41df41-9eea-44cd-ac1e-2f4d22c3ac10' # some random uuid
        url = reverse('sensor_detail', kwargs={'pk': pk})
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class MetricsDetailTest(TestData):
    def test_get_metrics_url(self):
        client = APIClient()
        client.credentials( HTTP_AUTHORIZATION='Token {}'.format(self.token1))
        sensor = self.metrics1.sensor
        url = reverse('metrics_detail', kwargs={'sensor': sensor})
        metrics = Metrics.objects.filter(sensor__name=sensor)
        serializer = SensorSerializer(metrics, many=True)
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
