# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicAppointment', '0017_auto_20151112_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='code',
            new_name='code_app',
        ),
    ]
