from django.db import models
from django.contrib.auth.models import User


class Providers(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    startyear = models.CharField(max_length=100, null=True)
    status = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Dealers(models.Model):
    dealerName = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    startdate = models.CharField(max_length=100, null=True)
    providername = models.ForeignKey(Providers, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.dealerName


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.name


class NumberCodes(models.Model):
    code = models.CharField(max_length=100, null=True)
    providerName = models.ForeignKey(Providers, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.code


class PhoneNumbers(models.Model):
    numbercode = models.ForeignKey(NumberCodes, null=True, on_delete=models.SET_NULL)
    phonenumber = models.CharField(max_length=100, null=True)
    categoryname = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.phonenumber


class Tarif(models.Model):
    name = models.CharField(max_length=100, null=True)
    tarifprovider = models.ForeignKey(Providers, null=True, on_delete=models.SET_NULL)
    status = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    phonenumber = models.ForeignKey(PhoneNumbers, null=True, on_delete=models.SET_NULL)
    

