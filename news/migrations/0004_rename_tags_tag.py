# Generated by Django 4.0.4 on 2022-05-26 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tags',
            new_name='tag',
        ),
    ]