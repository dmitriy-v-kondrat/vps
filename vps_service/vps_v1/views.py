from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from vps_v1.models import VPS
from vps_v1.serializers import VPSSerializer, ChoiceStatusVPSSerializer

"""
• создать VPS

• получить VPS по uid

• получить список VPS с возможностью фильтрации по параметрам

• перевести VPS в другой статус
"""


class CreateVPS(CreateAPIView):
    """Создаем VPS. """
    serializer_class = VPSSerializer


class RetrieveVPS(RetrieveAPIView):
    """Получаем экземпляр по uid. """
    serializer_class = VPSSerializer
    queryset = VPS.objects.all()
    lookup_field = 'uid'


class ListVPS(ListAPIView):
    """Список VPS с фильтрацией по параметрам. """
    serializer_class = VPSSerializer
    queryset = VPS.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uid', 'cpu', 'ram', 'hdd', 'status']


class ChoiceStatusVPS(UpdateAPIView):
    """Меняем статус VPS. """
    serializer_class = ChoiceStatusVPSSerializer
    queryset = VPS.objects.all()
    lookup_field = 'uid'
