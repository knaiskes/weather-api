from .base_tests import TestData
from api.models import Sensor, Metrics

class SensorTestCase(TestData):
    def test_str(self):
        sensor1 = Sensor.objects.get(name='Sensor1')
        sensor2 = Sensor.objects.get(name='Sensor2')

        self.assertEqual(str(sensor1), '%s - %s' % (sensor1.name, sensor1.board))
        self.assertEqual(str(sensor2), '%s - %s' % (sensor2.name, sensor2.board))


class MetricsTestCase(TestData):
    def test_str(self):
        metrics1 = Metrics.objects.get(id=self.metrics1.id)
        metrics2 = Metrics.objects.get(id=self.metrics2.id)

        self.assertEqual(str(metrics1), 'Metrics by %s sensor' % (metrics1.sensor))
        self.assertEqual(str(metrics2), 'Metrics by %s sensor' % (metrics2.sensor))
