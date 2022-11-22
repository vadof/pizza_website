from django.shortcuts import render
from pizza.menu_storage.pizza_storage import pizzas


def index(request):
    return render(request, 'pizza/index.html')

def pizza_menu(request):
    return render(request, 'pizza/menu/pizza.html', {'pizzas': pizzas, 'title': 'Pizza menu'})

def burger_menu(request):
    return render(request, 'pizza/menu/burger.html')

def drinks_menu(request):
    return render(request, 'pizza/menu/drinks.html')
