from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
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

        # Users
        cls.user1 = User.objects.create_user('testUser', 'testUser@test.com', 'testPass')

        # Tokens
        cls.token1, _ = Token.objects.get_or_create(user=cls.user1)
