# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-19 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='plans',
            field=models.CharField(choices=[('price_1NaqCpJqwQehDf1D2fgPtCRl', 'Monthly - £24.99'), ('price_1Nbt7BJqwQehDf1DvXF27HSf', '3 Months - £49.99'), ('price_1Naq9OJqwQehDf1DlaD7TCtL', '6 Months - £74.99')], default='price_1Naq9OJqwQehDf1DlaD7TCtL', max_length=100),
        ),
    ]
