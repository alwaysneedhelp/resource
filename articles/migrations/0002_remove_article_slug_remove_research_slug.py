# Generated by Django 5.1.1 on 2024-09-25 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='research',
            name='slug',
        ),
    ]
