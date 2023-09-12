from django.urls import path
from .views import homePage, categoryView, product_detail

app_name = 'products'

urlpatterns = [
    path('detail/<int:id>/', product_detail, name='detail'),
    path('<slug:category_slug>/', categoryView, name='category'),
    path('', homePage, name='home'),

]