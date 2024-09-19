from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from fruits.models import Fruit


def list_fruits(request):
    fruits = Fruit.objects.all()
    for fruit in fruits:
        print(fruit.fresh_fruit)
    return render(
        request, 
        'list_fruits.html', 
        { 'fruits': fruits }
        )


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.is_superuser:
                return redirect('admin:index') 
            else:
                return redirect('list_fruits')
        else:
            error = form.errors
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def sales_view(request):
   
    return render(request, 'sales.html')


