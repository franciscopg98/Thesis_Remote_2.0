# Generated by Django 4.0.4 on 2022-05-28 16:52

import datetime
import django.core.validators
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
                ('ingestiondate', models.DateTimeField(default=datetime.datetime(2022, 5, 28, 17, 52, 18, 213528))),
                ('orbitnumber', models.IntegerField(null=True)),
                ('lastorbitnumber', models.IntegerField(null=True)),
                ('relativeorbitnumber', models.IntegerField(null=True)),
                ('lastrelativeorbitnumber', models.IntegerField(null=True)),
                ('orbitdirection', models.CharField(choices=[('Ascending', 'Ascending'), ('Descending', 'Descending')], default='Ascending', max_length=25)),
                ('cloud_coverage', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('identifier', models.OneToOneField(default='S_2.Query', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s_related', serialize=False, to='basic_app.query')),
            ],
            bases=('basic_app.query',),
        ),
    ]