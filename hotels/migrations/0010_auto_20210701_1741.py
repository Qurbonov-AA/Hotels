# Generated by Django 3.2.4 on 2021-07-01 12:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_auto_20210701_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='hotel',
        ),
        migrations.AlterField(
            model_name='hotels',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 1, 17, 41, 46, 705469)),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels'),
        ),
        migrations.AlterField(
            model_name='services',
            name='dates',
            field=models.DateField(default=datetime.datetime(2021, 7, 1, 17, 41, 46, 706468)),
        ),
    ]
