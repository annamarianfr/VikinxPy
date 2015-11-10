# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0007_auto_20151110_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'f64303be7ffe842a5f76e25b5f8f7259bc166fd6ebd1f73855199456cea85d2c', max_length=100),
        ),
    ]
