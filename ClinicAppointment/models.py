from django.db import models

# Create your models here.
class Clinics(models.Model):
    name_clinic = models.CharField(max_length=100)
    lati = models.FloatField(default=0)
    longi = models.FloatField(default=0)
    def __unicode__(self):
    	return self.name_clinic