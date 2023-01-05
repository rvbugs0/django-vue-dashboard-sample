from rest_framework import serializers

from .models import WeatherInfo

class WeatherInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherInfo
        fields = ('temperature', 'date_recorded')