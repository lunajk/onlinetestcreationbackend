# Generated by Django 5.1.5 on 2025-03-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_remove_test_created_at_remove_test_is_ongoing_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='allow_feedback',
        ),
        migrations.RemoveField(
            model_name='test',
            name='time_limit',
        ),
        migrations.AddField(
            model_name='test',
            name='number_of_retakes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test',
            name='time_limit_per_question',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='test',
            name='total_time_limit',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
