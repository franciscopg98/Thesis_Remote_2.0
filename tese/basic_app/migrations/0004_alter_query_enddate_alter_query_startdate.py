# Generated by Django 4.0.4 on 2022-05-28 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_alter_query_enddate_alter_query_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='enddate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 17, 53, 4, 212326)),
        ),
        migrations.AlterField(
            model_name='query',
            name='startdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 17, 53, 4, 212326)),
        ),
    ]