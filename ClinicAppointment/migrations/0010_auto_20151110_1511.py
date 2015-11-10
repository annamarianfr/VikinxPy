# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0009_auto_20151110_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'ea716c29b45d7ac2d92d4c1afe5cef6889b2570186a7137ab2e8010d08e0d654', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default=b'W', max_length=1, choices=[(b'W', b'waiting'), (b'C', b'confirmed'), (b'F', b'finalized')]),
        ),
    ]
