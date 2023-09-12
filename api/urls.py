from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view()),
    path('<int:pk>/', views.ProductView.as_view()),
    path('category/', views.CategorysView.as_view()),
    path('category/<int:pk/', views.CategoryView.as_view()),
    ]