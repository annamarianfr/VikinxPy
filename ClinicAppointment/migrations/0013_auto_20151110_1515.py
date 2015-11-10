# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0012_auto_20151110_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'51c5540d66d296353db7459fc104b970fd476241138ece0ecd042f09bffbe857', max_length=100),
        ),
    ]
