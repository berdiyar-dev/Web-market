from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUserF
# Create your views here.

def RegistrationView(request):
    form = CreateUserF()

    if request.method == "POST":
        form = CreateUserF(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'acounts/register.html', context)

def LogoutPage(request):
    logout(request)
    return redirect('products:home')
def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products:home')

    context = {}
    return render(request, 'acounts/login.html', context)