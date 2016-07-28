# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 18:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=128)),
                ('photoUrl', models.URLField(blank=True, default='http://www.aspirehire.co.uk/aspirehire-co-uk/_img/profile.svg')),
                ('profile', models.CharField(blank=True, default='', max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
