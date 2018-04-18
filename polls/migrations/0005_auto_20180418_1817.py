# Generated by Django 2.0.4 on 2018-04-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180418_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='weathersearch',
            name='lat',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
        migrations.AddField(
            model_name='weathersearch',
            name='lon',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
    ]