from rest_framework import serializers;
from geodata.models import Shape;

class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = '__all__'
