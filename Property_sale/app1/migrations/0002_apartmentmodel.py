# Generated by Django 2.0.1 on 2019-10-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentModel',
            fields=[
                ('flatno', models.IntegerField(primary_key=True, serialize=False)),
                ('apname', models.CharField(max_length=50)),
                ('aplocation', models.CharField(max_length=100)),
                ('areasqft', models.IntegerField()),
                ('costpsqft', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maintcost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('facing', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('totalcost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
