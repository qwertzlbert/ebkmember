# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20170130_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='fee',
            field=models.FloatField(choices=[('24', '24'), ('18', 'reduced'), ('5', 'sustain_min'), ('0', 'other'), ('0', 'sustain_other')]),
        ),
    ]
