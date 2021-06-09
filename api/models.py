from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price= models.FloatField(null=True)
    company = models.CharField(max_length=100, null=True)
    duedate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
