# Generated by Django 3.2.4 on 2021-07-07 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0015_auto_20210707_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guests',
            options={'verbose_name': 'Гость', 'verbose_name_plural': '5.ФИО Госты'},
        ),
        migrations.AddField(
            model_name='guests',
            name='date1',
            field=models.DateField(default=datetime.datetime(2021, 7, 7, 13, 32, 16, 754299)),
        ),
        migrations.AddField(
            model_name='guests',
            name='date2',
            field=models.DateField(default=datetime.datetime(2021, 7, 7, 13, 32, 16, 754299)),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 7, 13, 32, 16, 751301)),
        ),
    ]
