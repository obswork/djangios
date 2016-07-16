# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('data_type', models.CharField(max_length=100)),
                ('data_value', models.FloatField()),
            ],
        ),
    ]