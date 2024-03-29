# Generated by Django 2.0.1 on 2019-10-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_apartmentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('eemail', models.EmailField(max_length=100)),
                ('elocation', models.CharField(max_length=30)),
                ('edoj', models.DateField()),
                ('erole', models.CharField(max_length=30)),
                ('eremark', models.CharField(max_length=30)),
            ],
        ),
    ]
