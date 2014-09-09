# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='file',
            name='docfile',
            field=models.FileField(default=None, upload_to=b'csv/'),
            preserve_default=False,
        ),
    ]
