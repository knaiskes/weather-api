from django.test import TestCase
from api.models import Sensor, Metrics

class TestData(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Sensors
        cls.sensor1 = Sensor.objects.create(name='Sensor1', room='Bedroom', board='Esp8266')
        cls.sensor2 = Sensor.objects.create(name='Sensor2', room='Kitchen', board='Esp8266')

        # Metrics
        cls.metrics1 = Metrics.objects.create(temperature=18.3, humidity=40.32, sensor=cls.sensor1)
        cls.metrics2 = Metrics.objects.create(temperature=20.9, humidity=60.10, sensor=cls.sensor2)

class SensorTestCase(TestData):
    def test_str(self):
        sensor1 = Sensor.objects.get(name='Sensor1')
        sensor2 = Sensor.objects.get(name='Sensor2')

        self.assertEqual(str(sensor1), '%s - %s' % (sensor1.name, sensor1.board))
