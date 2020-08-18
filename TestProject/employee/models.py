from django.db import models


# Create your models here.


class Department(models.Model):
    department = models.CharField(max_length=50)
    department_id = models.IntegerField()

    def __str__(self):
        return self.department


class Employee(models.Model):
    Employee_Id = models.IntegerField()
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
