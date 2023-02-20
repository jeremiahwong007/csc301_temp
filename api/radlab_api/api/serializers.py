from api.models import BreathingData
from rest_framework import serializers

class BreathingDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = BreathingData
        fields = ['id', 'data']