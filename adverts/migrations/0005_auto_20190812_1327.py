# Generated by Django 2.2.3 on 2019-08-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0004_auto_20190812_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Vehicle image'),
        ),
    ]
