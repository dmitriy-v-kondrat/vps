"""Адреса страниц"""

from django.urls import path

from vps_v2.views import CreateVPS, RetrieveVPS, ListVPS, ChoiceStatusVPS

urlpatterns = [
    path('create-vps-v2/', CreateVPS.as_view(), name='create_vps_v2'),
    path('retrive-vps-v2/<uid>/', RetrieveVPS.as_view(), name='retrive_vps_v2'),
    path('list-vps-v2/', ListVPS.as_view(), name='list_vps_v2'),
    path('choice-status-vps-v2/<uid>/', ChoiceStatusVPS.as_view(), name='choice_status_vps_v2'),
]
