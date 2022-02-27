from api.models import Sensor
from api.serializers import SensorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class SensorList(APIView):
    '''
    List all sensors
    '''
    def get(self, request, format=None):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)
