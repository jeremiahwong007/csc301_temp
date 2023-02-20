from django.shortcuts import render, get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.models import BreathingData
from api.serializers import BreathingDataSerializer

# radlab api views

# List all breathing data
class ListBreathingDataView(ListAPIView):
    queryset = BreathingData.objects.all()
    serializer_class = BreathingDataSerializer


# Retrieve specific breathing data by id
class RetrieveBreathingDataView(RetrieveAPIView):
    queryset = BreathingData.objects.all()
    serializer_class = BreathingDataSerializer
    lookup_field = 'pk'

    def get_object(self):
        return get_object_or_404(BreathingData, id=self.kwargs['pk'])