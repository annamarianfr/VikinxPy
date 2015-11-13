from random import randrange
from django.db import models
import os
import django
from django.conf import settings
from django.core.mail import send_mail
from kick_starter_python.settings import EMAIL_HOST_USER 
SEX=(("M","masculin"),("F","feminin"))
STATUS=(("Waiting","Waiting"),("Confirmed","Confirmed"),("Finalized","Finalized"))
CHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZabcdefghijklmnopqrstuvwxyz'
LENGTH = 6
MAX_TRIES = 32
# Create your models here.
class Clinic(models.Model):
    name_clinic = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def __unicode__(self):
        return str(self.id)+". "+self.name_clinic

class Appointment(models.Model):
    clinic_app=models.ForeignKey(Clinic)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(choices=SEX,max_length=1)
    CNP = models.CharField(max_length=13)
    date1 = models.CharField(max_length=50)
    date2 = models.CharField(max_length=50)
    date3 = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    status = models.CharField(choices=STATUS,max_length=10,default="Waiting")
    date_fin=models.CharField(max_length=50,default="Choose a date")
    code_app = models.CharField(max_length=10,default="123456")


    def __unicode__(self):
        return str(self.id)+". "+self.first_name+" "+self.last_name
    
    def save(self, *args, **kwargs):
        #send_mail('Test1','Test',settings.EMAIL_HOST_USER,['annamarianfr@gmail.com'],fail_silently=False)
        if (self.code_app=="123456"):
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ''
                    for i in range(LENGTH):
                        new_code += CHARSET[randrange(0, len(CHARSET))]
                    if not Appointment.objects.filter(code_app=new_code):
                        self.code_app = new_code
                        unique = True
                    loop_num += 1
                else:
                    raise ValueError("Couldn't generate a unique code.")
        if self.id:
            old_app = Appointment.objects.get(pk=self.id)
            if (old_app.status=="Waiting" and self.status == "Confirmed"):
                send_mail('Appointment Confirmed','This is a confirmation email to your appointment. \nLooking forward to your presence on %s '%(self.date_fin),EMAIL_HOST_USER,[self.email],fail_silently=False)
            elif (old_app.status == "Confirmed" and self.status == "Finalized"):
                send_mail('Appointment Finalized','Appointment finalized! Thank you for using Clinic@Point!',EMAIL_HOST_USER,[self.email],fail_silently=False)
        super(Appointment, self).save(*args, **kwargs)