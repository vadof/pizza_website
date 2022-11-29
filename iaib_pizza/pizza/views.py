from django.shortcuts import render

from .models import Pizza, Burger, Drink


def index(request):
    return render(request, 'pizza/index.html')

def pizza_menu(request):
    menu = Pizza.objects.all()
    return render(request, 'pizza/menu/pizza.html', {'menu': menu, 'title': 'Pizza menu'})

def burger_menu(request):
    menu = Burger.objects.all()
    return render(request, 'pizza/menu/burger.html', {'menu': menu, 'title': 'Burger menu'})

def drinks_menu(request):
    menu = Drink.objects.all()
    return render(request, 'pizza/menu/drinks.html', {'menu': menu, 'title': 'Drinks menu'})

def cart(request):
    return render(request, 'pizza/cart.html', {'title': 'Cart'})
