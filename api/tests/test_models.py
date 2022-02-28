from .base_tests import TestData
from api.models import Sensor, Metrics

class SensorTestCase(TestData):
    def test_str(self):
        sensor1 = Sensor.objects.get(name='Sensor1')
        sensor2 = Sensor.objects.get(name='Sensor2')

        self.assertEqual(str(sensor1), '%s - %s' % (sensor1.name, sensor1.board))
