from django.shortcuts import render

from pizza.menu_storage.pizza_menu import pizzas
from pizza.menu_storage.burger_menu import burgers
from pizza.menu_storage.drinks_menu import drinks


def index(request):
    return render(request, 'pizza/index.html')

def pizza_menu(request):
    return render(request, 'pizza/menu/pizza.html', {'pizzas': pizzas, 'title': 'Pizza menu'})

def burger_menu(request):
    return render(request, 'pizza/menu/burger.html', {'burgers': burgers, 'title': 'Burger menu'})

def drinks_menu(request):
    return render(request, 'pizza/menu/drinks.html', {'drinks': drinks, 'title': 'Drinks menu'})
