"""Адреса страниц"""

from django.urls import path

from vps_v1.views import CreateVPS, RetrieveVPS, ListVPS, ChoiceStatusVPS

urlpatterns = [
    path('create-vps-v1/', CreateVPS.as_view(), name='create_vps_v1'),
    path('retrive-vps-v1/<uid>/', RetrieveVPS.as_view(), name='retrive_vps_v1'),
    path('list-vps-v1/', ListVPS.as_view(), name='list_vps_v1'),
    path('choice-status-vps-v1/<uid>/', ChoiceStatusVPS.as_view(), name='choice_status_vps_v1'),
]
