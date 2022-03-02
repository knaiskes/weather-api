from .base_tests import TestData
from django.urls import reverse
from rest_framework import status
from api.models import Sensor, Metrics
from api.serializers import SensorSerializer

class SensorListTest(TestData):
    def test_get_all_sensors(self):
        url = reverse('sensor_list')
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
