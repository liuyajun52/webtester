# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_type', models.CharField(max_length=12)),
                ('url', models.CharField(max_length=1024)),
                ('text', models.CharField(max_length=1024)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Case')),
            ],
        ),
    ]