# Generated by Django 3.2.4 on 2021-06-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20210606_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=28),
        ),
        migrations.AlterField(
            model_name='employee',
            name='login',
            field=models.CharField(max_length=28),
        ),
    ]
