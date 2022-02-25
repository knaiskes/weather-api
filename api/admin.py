from django.contrib import admin
from .models import Sensor, Metrics

admin.site.register(Sensor)
admin.site.register(Metrics)
