# Generated by Django 4.0 on 2022-01-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
