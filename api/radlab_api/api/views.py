from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from api.models import BreathingData
from api.serializers import BreathingDataSerializer

# radlab api views

# Create breathing data
class CreateBreathingDataView(generics.CreateAPIView):
    serializer_class = BreathingDataSerializer


# List all breathing data
class ListBreathingDataView(generics.ListAPIView):
    queryset = BreathingData.objects.all()
    serializer_class = BreathingDataSerializer


# Retrieve specific breathing data by id
class RetrieveBreathingDataView(generics.RetrieveAPIView):
    queryset = BreathingData.objects.all()
    serializer_class = BreathingDataSerializer
    lookup_field = 'pk'

    def get_object(self):
        return get_object_or_404(BreathingData, id=self.kwargs['pk'])

