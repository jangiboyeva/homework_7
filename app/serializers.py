from rest_framework import serializers
from .models import Logo,Main,Detail,Country_detail

class LogoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['phone','telegram','image']


class MainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'

class DetailSerializers(serializers.Serializer):
    class Meta:
        model = Detail
        fields = '__all__'

class CountrydetailSerializers(serializers.Serializer):
    model = Country_detail
    fields = '__all__'