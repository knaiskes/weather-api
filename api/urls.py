from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('sensors/', views.SensorList.as_view(), name='sensor_list'),
    path('sensors/<uuid:pk>', views.SensorDetail.as_view(), name='sensor_detail'),
    path('metrics/<str:sensor>', views.MetricsDetail.as_view(), name='metrics_detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
