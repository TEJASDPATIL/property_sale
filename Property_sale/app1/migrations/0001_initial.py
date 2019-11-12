# Generated by Django 2.0.1 on 2019-10-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlotModel',
            fields=[
                ('plotno', models.IntegerField(primary_key=True, serialize=False)),
                ('roadno', models.IntegerField()),
                ('surveyno', models.IntegerField()),
                ('areasqyrd', models.FloatField()),
                ('costpryard', models.DecimalField(decimal_places=2, max_digits=10)),
                ('otherexp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('boundaries', models.IntegerField()),
                ('facing', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('totalcost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
