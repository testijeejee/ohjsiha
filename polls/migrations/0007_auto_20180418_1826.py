# Generated by Django 2.0.4 on 2018-04-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180418_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weathersearch',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='weathersearch',
            name='lon',
            field=models.FloatField(default=0.0),
        ),
    ]
