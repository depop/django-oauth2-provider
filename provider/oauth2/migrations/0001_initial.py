# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import provider.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                (
                    'id',
                    models.AutoField(
                        verbose_name='ID',
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    'token',
                    models.CharField(
                        default=provider.utils.long_token, max_length=255, db_index=True
                    ),
                ),
                ('expires', models.DateTimeField()),
                (
                    'scope',
                    models.IntegerField(
                        default=2,
                        choices=[(2, b'read'), (4, b'write'), (6, b'read+write')],
                    ),
                ),
            ],
            options={'get_latest_by': 'expires'},
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                (
                    'id',
                    models.AutoField(
                        verbose_name='ID',
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ('name', models.CharField(max_length=255, blank=True)),
                ('url', models.URLField(help_text=b"Your application's URL.")),
                (
                    'redirect_uri',
                    models.URLField(help_text=b"Your application's callback URL"),
                ),
                (
                    'client_id',
                    models.CharField(
                        default=provider.utils.short_token, max_length=255
                    ),
                ),
                (
                    'client_secret',
                    models.CharField(default=provider.utils.long_token, max_length=255),
                ),
                (
                    'client_type',
                    models.IntegerField(
                        choices=[
                            (0, b'Confidential (Web applications)'),
                            (1, b'Public (Native and JS applications)'),
                        ]
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        related_name='oauth2_client',
                        blank=True,
                        to=settings.AUTH_USER_MODEL,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                (
                    'id',
                    models.AutoField(
                        verbose_name='ID',
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    'code',
                    models.CharField(default=provider.utils.long_token, max_length=255),
                ),
                (
                    'expires',
                    models.DateTimeField(default=provider.utils.get_code_expiry),
                ),
                ('redirect_uri', models.CharField(max_length=255, blank=True)),
                ('scope', models.IntegerField(default=0)),
                (
                    'client',
                    models.ForeignKey(related_name='oauth2_grant', to='oauth2.Client'),
                ),
                (
                    'user',
                    models.ForeignKey(
                        default=None, to=settings.AUTH_USER_MODEL, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='LoginAttempt',
            fields=[
                (
                    'id',
                    models.AutoField(
                        verbose_name='ID',
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ('username', models.CharField(max_length=75, db_index=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('success', models.BooleanField(default=False)),
                ('ip_address', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                (
                    'id',
                    models.AutoField(
                        verbose_name='ID',
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    'token',
                    models.CharField(
                        default=provider.utils.long_token, max_length=255, db_index=True
                    ),
                ),
                ('expired', models.BooleanField(default=False)),
                (
                    'access_token',
                    models.OneToOneField(
                        related_name='refresh_token', to='oauth2.AccessToken'
                    ),
                ),
                (
                    'client',
                    models.ForeignKey(related_name='refresh_token', to='oauth2.Client'),
                ),
                (
                    'user',
                    models.ForeignKey(
                        default=None, to=settings.AUTH_USER_MODEL, null=True
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='client',
            field=models.ForeignKey(
                related_name='oauth2_accesstoken', to='oauth2.Client'
            ),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(
                default=None, to=settings.AUTH_USER_MODEL, null=True
            ),
        ),
    ]
