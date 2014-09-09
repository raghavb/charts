# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('stock_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('file_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
