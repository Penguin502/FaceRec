# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='peInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('peName', models.CharField(max_length=20)),
                ('idNum', models.CharField(max_length=17)),
                ('sex', models.CharField(max_length=4)),
                ('pict', models.TextField()),
                ('feapict', models.TextField()),
            ],
        ),
    ]
