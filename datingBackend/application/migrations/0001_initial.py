# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Id', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('age', models.IntegerField(blank=True)),
                ('sex', models.CharField(max_length=6)),
                ('height', models.FloatField(blank=True)),
                ('weight', models.IntegerField(blank=True)),
                ('body_type', models.CharField(max_length=10)),
                ('ehtnicity', models.CharField(max_length=20)),
                ('music', models.CharField(max_length=20)),
                ('food_habits', models.CharField(max_length=20)),
                ('drinking', models.BooleanField()),
                ('smoking', models.BooleanField()),
                ('photo', models.ImageField(blank=True, upload_to=b'')),
            ],
        ),
    ]