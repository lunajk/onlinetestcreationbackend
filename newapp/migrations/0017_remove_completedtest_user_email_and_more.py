# Generated by Django 5.1.5 on 2025-02-17 10:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0016_alter_completedtest_time_taken'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedtest',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='completedtest',
            name='user_name',
        ),
        migrations.AddField(
            model_name='completedtest',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
