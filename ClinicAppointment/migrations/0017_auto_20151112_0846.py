# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0016_auto_20151111_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date3',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default=b'waiting', max_length=10, choices=[(b'Waiting', b'Waiting'), (b'Confirmed', b'Confirmed'), (b'Finalized', b'Finalized')]),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time3',
            field=models.CharField(max_length=20),
        ),
    ]
