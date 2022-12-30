from django.shortcuts import render
from rest_framework import viewsets
from nasa.models import Nasa
from nasa.serializers import NasaSerializer

# Create your views here.


class NasaViewSet(viewsets.ModelViewSet):

    queryset = Nasa.objects.all()
    serializer_class = NasaSerializer
    filterset_fields = ['due_data']
    search_fields = ['title']
