from django.db import models

class PlotModel(models.Model):
    plotno = models.IntegerField(primary_key=True)
    roadno = models.IntegerField()
    surveyno = models.IntegerField()
    areasqyrd = models.FloatField()
    costpryard = models.DecimalField(max_digits=10,decimal_places=2)
    otherexp = models.DecimalField(max_digits=10,decimal_places=2)
    boundaries = models.IntegerField()

    facing = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    totalcost = models.DecimalField(max_digits=10,decimal_places=2)

class ApartmentModel(models.Model):
    flatno = models.IntegerField(primary_key=True)
    apname = models.CharField(max_length=50)
    aplocation = models.CharField(max_length=100)
    areasqft = models.IntegerField()
    costpsqft = models.DecimalField(max_digits=10,decimal_places=2)
    maintcost = models.DecimalField(max_digits=10,decimal_places=2)
    facing = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    totalcost = models.DecimalField(max_digits=10,decimal_places=2)

class EmployeeModel(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    eemail = models.EmailField(max_length=100)
    elocation = models.CharField(max_length=30)
    edoj = models.DateField()
    erole = models.CharField(max_length=30)
    eremark = models.CharField(max_length=30)
