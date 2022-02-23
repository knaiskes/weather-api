from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    room = models.CharField(max_length=50)
    board = models.CharField(max_length=20)

    def __str__(self):
        return '%s - %s' % (self.name, self.board)
