# Generated by Django 4.0.4 on 2022-05-28 16:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('ingestiondate', models.DateTimeField(default=datetime.datetime(2022, 5, 28, 17, 52, 18, 209530))),
                ('orbitnumber', models.IntegerField(null=True)),
                ('lastorbitnumber', models.IntegerField(null=True)),
                ('relativeorbitnumber', models.IntegerField(null=True)),
                ('lastrelativeorbitnumber', models.IntegerField(null=True)),
                ('orbitdirection', models.CharField(choices=[('Ascending', 'Ascending'), ('Descending', 'Descending')], default='Ascending', max_length=25)),
                ('timeliness', models.CharField(choices=[('NRT', 'NRT-3h'), ('NTC', 'Fast-24h')], default='Ascending', max_length=25)),
                ('polarization', models.CharField(choices=[('HH', 'HH'), ('VV', 'VV'), ('HV', 'HV'), ('VH', 'VH'), ('HH HV', 'HH HV'), ('VV VH', 'VV VH')], default='HH', max_length=15)),
                ('swath_identifier', models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('IW', 'IW'), ('IW1', 'IW1'), ('IW2', 'IW2'), ('IW3', 'IW3'), ('EW', 'EW'), ('EW1', 'EW1'), ('EW2', 'EW2'), ('EW3', 'EW3'), ('EW4', 'EW4'), ('EW5', 'EW5')], default='S1', max_length=15)),
                ('sensor_operational_mode', models.CharField(choices=[('SM', 'SM'), ('IW', 'IW'), ('EW', 'EW'), ('WV', 'WV')], default='SM', max_length=15)),
                ('identifier', models.OneToOneField(default='S_1.Query', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s_related', serialize=False, to='basic_app.query')),
            ],
            bases=('basic_app.query',),
        ),
    ]
