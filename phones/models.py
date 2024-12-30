from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.IntegerField()
    storage = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CustomUser (AbstractUser ):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


