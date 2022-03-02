from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('sensors/', views.SensorList.as_view(), name='sensor_list'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
