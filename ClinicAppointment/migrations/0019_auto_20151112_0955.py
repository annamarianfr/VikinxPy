# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0018_auto_20151112_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default=b'Waiting', max_length=10, choices=[(b'Waiting', b'Waiting'), (b'Confirmed', b'Confirmed'), (b'Finalized', b'Finalized')]),
        ),
    ]
