from django.db import models
import os
SEX=(("M","masculin"),("F","feminin"))
STATUS=(("W","waiting"),("C","confirmed"),("F","finalized"))
# Create your models here.
class Clinic(models.Model):
    name_clinic = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    def __unicode__(self):
        return self.name_clinic

class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(choices=SEX,max_length=1)
    CNP = models.CharField(max_length=13)
    date1 = models.DateField(auto_now=False, auto_now_add=False)
    date2 = models.DateField(auto_now=False, auto_now_add=False)
    date3 = models.DateField(auto_now=False, auto_now_add=False)
    time1 = models.TimeField(auto_now=False, auto_now_add=False)
    time2 = models.TimeField(auto_now=False, auto_now_add=False)
    time3 = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=200)
    status = models.CharField(choices=STATUS,max_length=1,default="W")
    code = models.CharField(max_length=100,default=os.urandom(32).encode('hex'))
    def __unicode__(self):
        return str(self.id)+". "+self.first_name+" "+self.last_name