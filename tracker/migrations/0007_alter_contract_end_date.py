# Generated by Django 3.2.4 on 2021-06-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20210610_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='end_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
