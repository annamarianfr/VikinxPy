# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0015_auto_20151111_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default=b'waiting', max_length=10, choices=[(b'waiting', b'W'), (b'confirmed', b'C'), (b'finalized', b'F')]),
        ),
    ]
