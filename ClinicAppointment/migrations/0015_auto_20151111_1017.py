# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0014_auto_20151111_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
