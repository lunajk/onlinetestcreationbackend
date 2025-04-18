# Generated by Django 5.1.5 on 2025-02-18 08:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0017_remove_completedtest_user_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userresponse',
            old_name='name',
            new_name='test_name',
        ),
        migrations.RenameField(
            model_name='userresponse',
            old_name='email',
            new_name='user_email',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='responses',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='attempts',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userresponse',
            name='correct',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userresponse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userresponse',
            name='incorrect',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userresponse',
            name='question',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userresponse',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='user_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
