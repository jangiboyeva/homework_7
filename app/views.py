from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Logo,Main,Detail,Country_detail
from .serializers import LogoSerializers,MainSerializers,DetailSerializers,CountrydetailSerializers

# Create your views here.
class LogoView(ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializers

class MainView(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializers

class DetailView(ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializers

class DetailcountryView(ModelViewSet):
    queryset = Country_detail.objects.all()
    serializer_class = CountrydetailSerializers