from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    birth_date = models.DateField()
    salary = models.IntegerField()
    receipt_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname