# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0019_auto_20151112_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time1',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time2',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time3',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date_fin',
            field=models.CharField(default=b'Choose a date', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date3',
            field=models.CharField(max_length=50),
        ),
    ]
