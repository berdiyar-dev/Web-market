from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    def __str__(self):
        return self.c_name

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    add_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return self.name

