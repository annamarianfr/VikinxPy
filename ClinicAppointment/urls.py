from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClinicListView,AppointmentListView, AppointmentDetailView


urlpatterns = [
    url(r'^clinic/$', ClinicListView.as_view(), name='clinic'),
    url(r'^appointment/$', AppointmentListView.as_view(), name='appointment'),
    #url(r'^appointment/(?P<pk>[0-9]+)/$', AppointmentDetailView.as_view(), name='appointment_details'),
    url(r'^appointment/(?P<code_app>[^/]+)/$', AppointmentDetailView.as_view(), name='appointment_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)