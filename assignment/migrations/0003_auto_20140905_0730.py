# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20140905_0713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_name',
            new_name='company',
        ),
    ]
