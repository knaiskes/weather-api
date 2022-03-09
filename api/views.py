from rest_framework.permissions import IsAuthenticated
from api.models import Sensor, Metrics
from api.serializers import SensorSerializer, MetricsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class SensorList(APIView):
    permission_classes = [IsAuthenticated]
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

class SensorDetail(APIView):
    permission_classes = [IsAuthenticated]
    '''
    GET, UPDATE and delete a sensor instance
    '''
    def get_object(self, pk):
        try:
            return Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sensor = self.get_object(pk)
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sensor = self.get_object(pk)
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sensor = self.get_object(pk)
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MetricsDetail(APIView):
    permission_classes = [IsAuthenticated]
    '''
    GET metrics by (sensor) sensor
    '''

    def get_object(self, sensor):
        try:
            return Metrics.objects.filter(sensor__name=sensor)
        except Metrics.DoesNotExist:
            raise Http404

    def get(self, request, sensor, format=None):
        metrics = self.get_object(sensor)
        serializer = MetricsSerializer(metrics, many=True)
        return Response(serializer.data)
