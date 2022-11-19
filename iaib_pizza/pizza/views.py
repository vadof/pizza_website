from django.shortcuts import render

def index(request):
    return render(request, 'pizza/index.html')

def pizza_menu(request):
    return render(request, 'pizza/menu/pizza.html')

def burger_menu(request):
    return render(request, 'pizza/menu/burger.html')

def drinks_menu(request):
    return render(request, 'pizza/menu/drinks.html')

def nav(request):
    return render(request, 'pizza/navbar.html')