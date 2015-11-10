# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0006_auto_20151110_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'b43ea4d4521afe08e31fd1e99fad365699945fff605296d9a87313541c429aee', max_length=100),
        ),
    ]
