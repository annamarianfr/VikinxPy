# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0008_auto_20151110_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'c2cd9c7ceae8f33c5d1995dc51948ddf26ad6f4ef3b5b56ffd46b2811b0242e1', max_length=100),
        ),
    ]
