# Generated by Django 4.0 on 2022-01-08 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AvailableService',
            new_name='Service',
        ),
    ]