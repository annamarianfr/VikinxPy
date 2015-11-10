# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0011_auto_20151110_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'f1ef22f4c23ffe908ad734e0a711c4f77d1dbe9c68ef6f40e2f6d5a69cd9eb10', max_length=100),
        ),
    ]
