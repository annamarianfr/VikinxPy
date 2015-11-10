# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0005_auto_20151110_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=b'6228c42bf77e2a61a8c18194c7467bc6bd57f870e149860e4df450d7e6ef8279', max_length=100),
        ),
    ]
