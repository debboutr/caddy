# Generated by Django 5.0.1 on 2024-01-26 03:00

import junk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loop',
            name='bags',
            field=models.FloatField(validators=[junk.models.validate_bags]),
        ),
    ]
