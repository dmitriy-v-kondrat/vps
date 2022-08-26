
from django.urls import path

from vps_v3.views import CreateVPS, RetrieveVPS, ListVPS, ChoiceStatusVPS

urlpatterns = [
    path('create-vps-v3/', CreateVPS.as_view(), name='create_vps_v3'),
    path('retrive-vps-v3/<uid>/', RetrieveVPS.as_view(), name='retrive_vps_v3'),
    path('list-vps-v3/', ListVPS.as_view(), name='list_vps_v3'),
    path('choice-status-vps-v3/<uid>/', ChoiceStatusVPS.as_view(), name='choice_status_vps_v3'),
]
