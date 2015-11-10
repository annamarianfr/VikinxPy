from django.conf.urls import url

from .views import ClinicsListView


urlpatterns = [
    url(r'$', ClinicsListView.as_view(), name='clinicsapp')
]
