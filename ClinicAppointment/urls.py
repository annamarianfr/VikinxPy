from django.conf.urls import url

from .views import ClinicListView,AppointmentListView


urlpatterns = [
    url(r'^clinic/', ClinicListView.as_view(), name='clinic'),
    url(r'^appointment/', AppointmentListView.as_view(), name='appointment'),
]
