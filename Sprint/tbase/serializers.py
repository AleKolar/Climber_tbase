from rest_framework import serializers

from .models import User, Coords, PerevalAdded, PerevalImages


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalAddedSerializer(serializers.ModelSerializer):
    status = serializers.CharField(default='new')

    class Meta:
        model = PerevalAdded
        fields = '__all__'


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'
