from django.shortcuts import render

from .models import Product


def index(request):
    return render(request, 'pizza/index.html')

def pizza_menu(request):
    menu = [product for product in Product.objects.all() if product.category_id == 1]
    print(menu)
    return render(request, 'pizza/menu/pizza.html', {'menu': menu, 'title': 'Pizza menu'})

def burger_menu(request):
    menu = [product for product in Product.objects.all() if product.category_id == 2]
    return render(request, 'pizza/menu/burger.html', {'menu': menu, 'title': 'Burger menu'})

def drinks_menu(request):
    menu = [product for product in Product.objects.all() if product.category_id == 3]
    return render(request, 'pizza/menu/drinks.html', {'menu': menu, 'title': 'Drinks menu'})

def cart(request):
    return render(request, 'pizza/cart.html', {'title': 'Cart'})
