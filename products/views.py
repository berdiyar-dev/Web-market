from django.shortcuts import render
from .models import Category,Products
from django.views.generic import ListView, DetailView
from baskets.forms import CartAddProductForm
# Create your views here.
from django.shortcuts import render


class HomePage(ListView):
    model = Products
    template_name = 'products/home.html'
    context_object_name = 'products'

class DetailPage(DetailView):
    model = Products
    template_name = 'products/detail.html'
    context_object_name = 'product'

def categoryView(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products = Products.objects.filter(category=category)
    return render(request, 'products/name_category.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})

def homePage(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, template_name='products/home.html', context=context)

def product_detail(request, id):
    product = Products.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/detail.html', {'product': product, 'cart_product_form': cart_product_form})

