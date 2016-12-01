# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-23 10:01
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0005_auto_20160523_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('commented_at', models.DateTimeField(default=datetime.datetime(2016, 5, 23, 10, 1, 45, 144478, tzinfo=utc))),
                ('liked_at', models.DateTimeField(default=datetime.datetime(2016, 5, 23, 10, 1, 45, 144514, tzinfo=utc))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]