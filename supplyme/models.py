from django.db import models


class DateFields:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Organization(models.Model, DateFields):
    CST = 'CUSTOMER'
    PRV = 'PROVIDER'
    TYPE_CHOICES = (
        (CST, 'Customer'),
        (PRV, 'Provider'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, null=False)
    name = models.CharField(max_length=40, null=False)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=40, null=False)  # To be encrypted

    def __str__(self):
        return self.name


class User(models.Model, DateFields):
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=40, null=False)  # To be encrypted
    email  = models.CharField(max_length=20, null=False)  # To be encrypted
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=40, null=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model, DateFields):
    name = models.CharField(max_length=40, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False)
    price = models.FloatField(null=False)

    def __str__(self):
        return " - ".join((self.name, self.provider))
