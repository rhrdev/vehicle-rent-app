# Generated by Django 2.2.3 on 2019-07-26 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0006_auto_20190726_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='available_from',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
