# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0013_auto_20151110_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'123456', max_length=10),
        ),
    ]
