# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20170129_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='fee',
            field=models.FloatField(choices=[('24', 'normal'), ('18', 'reduced'), ('5', 'sustain_min'), ('0', 'other')]),
        ),
    ]
