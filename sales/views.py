
from django.shortcuts import render
from .models import Fruit


def create_sale(request):
    if request.method == "POST":
        fruit_name = request.POST.get("fruit_name")
        quantity_fruit = request.POST.get("quantity_fruit")
        print(fruit_name, quantity_fruit)

        fruits = Fruit.objects.filter(name__icontains = fruit_name)

        for fruit in fruits:
            print(fruit.value)

   
    return render(request, 'create_sale.html')
