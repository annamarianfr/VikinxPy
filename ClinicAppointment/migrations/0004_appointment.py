# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0003_auto_20151110_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(default=0, max_length=10)),
                ('age', models.IntegerField(max_length=2)),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'masculin'), (b'F', b'feminin')])),
                ('CNP', models.CharField(max_length=13)),
                ('date1', models.DateField()),
                ('date2', models.DateField()),
                ('date3', models.DateField()),
                ('time1', models.TimeField()),
                ('time2', models.TimeField()),
                ('time3', models.TimeField()),
                ('description', models.TextField(max_length=200)),
                ('status', models.CharField(max_length=1, choices=[(b'W', b'waiting'), (b'C', b'confirmed'), (b'F', b'finalized')])),
                ('code', models.CharField(max_length=100)),
            ],
        ),
    ]
