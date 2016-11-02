# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squawker2', '0002_auto_20161102_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squawks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squawk', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='postSquawks',
        ),
    ]
