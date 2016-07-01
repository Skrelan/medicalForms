# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-01 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=180)),
                ('uid', models.DecimalField(decimal_places=0, max_digits=10)),
                ('appointment', models.DateTimeField()),
            ],
        ),
    ]
