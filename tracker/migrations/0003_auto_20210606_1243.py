# Generated by Django 3.2.4 on 2021-06-06 12:43

from django.db import migrations, models
import tracker.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20210606_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default=tracker.models.Employee.create_email, max_length=28),
        ),
        migrations.AlterField(
            model_name='employee',
            name='login',
            field=models.CharField(default=tracker.models.Employee.create_login, max_length=28),
        ),
    ]
