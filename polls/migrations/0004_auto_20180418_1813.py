# Generated by Django 2.0.4 on 2018-04-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180418_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celsius', models.DecimalField(decimal_places=2, max_digits=2)),
                ('city', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-pub_date']},
        ),
    ]
