# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0005_auto_20140909_0052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='stock_id',
            new_name='stockId',
        ),
    ]
