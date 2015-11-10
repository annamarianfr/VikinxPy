# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_clinic', models.CharField(max_length=100)),
                ('lati', models.FloatField(default=0)),
                ('longi', models.FloatField(default=0)),
            ],
        ),
    ]
