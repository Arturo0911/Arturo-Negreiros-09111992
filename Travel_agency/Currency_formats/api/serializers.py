#from rest_framework import serializers
from Currency_formats.models import Country
from rest_framework_mongoengine import serializers 


class CountrySerializer(serializers.DocumentSerializer):

    class Meta:
        model = Country
        fields = '__all__'
