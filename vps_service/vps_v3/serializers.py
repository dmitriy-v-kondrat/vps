"""Сериализация модели"""
from rest_framework import serializers

from vps_v3.models import VPS


class VPSSerializer(serializers.ModelSerializer):
    """Сериализатор экземпляра модели"""

    class Meta:
        model = VPS
        fields = '__all__'


class ChoiceStatusVPSSerializer(serializers.ModelSerializer):
    """Сериализатор обновления экземпляра модели"""

    class Meta:
        model = VPS
        fields = ('status', )
