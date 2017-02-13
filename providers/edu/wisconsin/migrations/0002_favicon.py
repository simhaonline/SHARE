# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-01 21:23
from __future__ import unicode_literals

from django.db import migrations
import share.robot


class Migration(migrations.Migration):

    dependencies = [
        ('edu.wisconsin', '0001_initial'),
        ('share', '0018_store_favicons'),
    ]

    operations = [
        migrations.RunPython(
            code=share.robot.RobotFaviconMigration('edu.wisconsin'),
        ),
    ]
