# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]