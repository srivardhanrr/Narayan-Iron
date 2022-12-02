from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    image = models.CharField(max_length=5000, null=True, blank=True)


class Client(models.Model):
    client_name = models.CharField(max_length=200)
    image = models.CharField(max_length=5000, null=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.email


class Subscribe(models.Model):
    email = models.EmailField()

    def __str(self):
        return self.email
