from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
