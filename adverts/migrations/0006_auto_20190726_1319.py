# Generated by Django 2.2.3 on 2019-07-26 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0005_remove_advert_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_from',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
