# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-23 11:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0007_auto_20160523_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_at', models.DateTimeField(default=datetime.datetime(2016, 5, 23, 11, 37, 21, 746056, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='PostLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(default=datetime.datetime(2016, 5, 23, 11, 37, 21, 745418, tzinfo=utc))),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='postsocial',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='postsocial',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postsocial',
            name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='liked_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 23, 11, 37, 21, 744499, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='PostSocial',
        ),
        migrations.AddField(
            model_name='postlikes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.Post'),
        ),
        migrations.AddField(
            model_name='postlikes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.Post'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
