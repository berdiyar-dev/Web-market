from django.contrib import admin
from .models import Category, Products
# Register your models here.
@admin.register(Products)

class Products(admin.ModelAdmin):
    note_list = [
        'name',
        'price',
        'add_date'
    ]
    ordering = ('add_date',)

@admin.register(Category)
class Category(admin.ModelAdmin):
    note_list = ['c_name']
    ordering = ('c_name',)