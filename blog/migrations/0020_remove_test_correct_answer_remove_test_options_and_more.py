# Generated by Django 5.1.5 on 2025-02-26 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_test_correct_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='test',
            name='options',
        ),
        migrations.RemoveField(
            model_name='test',
            name='questions',
        ),
    ]
