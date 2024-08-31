from django.db import models

class employees(models.Model):  # Using plural form for the class name
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    emp_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.first_name
