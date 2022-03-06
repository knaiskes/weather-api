from api.models import Sensor
from api.serializers import SensorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SensorList(APIView):
    '''
    List all sensors or add a new one
    '''
    def get(self, request, format=None):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
