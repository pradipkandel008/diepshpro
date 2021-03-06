# Generated by Django 3.2.5 on 2022-01-09 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professionals', '0003_auto_20220109_1142'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Serv',
        ),
        migrations.AddField(
            model_name='servc',
            name='service_location',
            field=models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Bhaktapur', 'Bhaktapur'), ('Lalitpur', 'Lalitpur')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servc',
            name='service_type',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.service'),
        ),
        migrations.AddField(
            model_name='servc',
            name='service_user',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
