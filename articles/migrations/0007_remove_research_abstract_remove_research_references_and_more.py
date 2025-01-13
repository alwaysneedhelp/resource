# Generated by Django 5.1.1 on 2024-10-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_views_research_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='research',
            name='references',
        ),
        migrations.AddField(
            model_name='research',
            name='abstract_file',
            field=models.FileField(blank=True, null=True, upload_to='research/abstracts/'),
        ),
        migrations.AddField(
            model_name='research',
            name='references_file',
            field=models.FileField(blank=True, null=True, upload_to='research/references/'),
        ),
    ]
