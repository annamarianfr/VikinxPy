# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0021_appointment_clinic_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='clinic_app',
        ),
    ]
