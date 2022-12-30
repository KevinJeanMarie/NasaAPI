from rest_framework import serializers
from nasa.models import Nasa


class NasaSerializer(serializers.ModelSerializer):

    date = serializers.DateField(source='due_data')

    class Meta:
        model = Nasa
        exclude = ['due_data']
