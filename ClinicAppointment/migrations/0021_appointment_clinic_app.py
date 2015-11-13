# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0020_auto_20151112_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='clinic_app',
            field=models.ForeignKey(default=1, to='ClinicAppointment.Clinic'),
        ),
    ]
