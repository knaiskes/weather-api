from django.db import models
import uuid

class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    room = models.CharField(max_length=50)
    board = models.CharField(max_length=20)

    def __str__(self):
        return '%s - %s' % (self.name, self.board)

class Metrics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    temperature = models.FloatField()
    humidity = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return 'Metrics by %s sensor' % self.sensor
