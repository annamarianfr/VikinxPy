# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0010_auto_20151110_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'c9057a8dcada11600259feb9250bfbc43e27e872944c4c9ffcedcad270e547cd', max_length=100),
        ),
    ]
