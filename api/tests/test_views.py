from .base_tests import TestData
from django.urls import reverse
from rest_framework import status
from api.models import Sensor, Metrics
from api.serializers import SensorSerializer
from rest_framework.test import APIClient

class SensorListTest(TestData):
    def test_get_all_sensors(self):
        url = reverse('sensor_list')
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request(self):
        client = APIClient()
        url = reverse('sensor_list')
        response = client.post(url, {'name': 'Sensor3', 'room': 'Living Room', 'board': 'Esp32'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_sensor_bad_request(self):
        '''
        Violate unique name field constraint
        '''
        client = APIClient()
        url = reverse('sensor_list')
        response = client.post(url, {'name': 'Sensor1', 'room': 'Different Room', 'board': 'Esp32'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
