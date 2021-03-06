# Generated by Django 3.2.4 on 2021-07-01 05:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_alter_hotels_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='adress_google',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 1, 10, 33, 46, 658574)),
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('dates', models.DateField(default=datetime.datetime(2021, 7, 1, 10, 33, 46, 658574))),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels')),
            ],
        ),
    ]
