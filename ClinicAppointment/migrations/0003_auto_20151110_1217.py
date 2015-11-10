# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0002_auto_20151110_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='lati',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='longi',
            new_name='longitude',
        ),
    ]
