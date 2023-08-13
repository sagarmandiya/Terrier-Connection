# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20190621_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, default='1990-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='is_verified',
            field=models.CharField(choices=[('TO BE APPROVED', 'To be approved'), ('APPROVED', 'Approved'), ('NOT APPROVED', 'Not approved')], default='TO BE APPROVED', max_length=14),
        ),
    ]
