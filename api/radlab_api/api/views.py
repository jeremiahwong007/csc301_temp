from django.shortcuts import render
from rest_framework import generics
from serializers import BreathingDataSerializer
# Create your views here.

class CreateTrialData(generics.CreateAPIView):
    serializer_class = BreathingDataSerializer
