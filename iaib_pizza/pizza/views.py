from django.shortcuts import render, get_object_or_404

from .models import Product, Category
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'pizza/index.html')

def pizza_menu(request):
    menu = [product for product in Product.objects.all() if product.category_id == 1]
    return render(request, 'pizza/menu/pizza.html', {'menu': menu, 'title': 'Pizza menu'})

def burger_menu(request):
    menu = [product for product in Product.objects.all() if product.category_id == 2]
    return render(request, 'pizza/menu/burger.html', {'menu': menu, 'title': 'Burger menu'})

def drinks_menu(request):
    menu = [product for product in Product.objects.all() if product.category_id == 3]
    return render(request, 'pizza/menu/drinks.html', {'menu': menu, 'title': 'Drinks menu'})

def cart(request):
    return render(request, 'iaib_pizza/cart/detail.html', {'title': 'Cart'})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'iaib_pizza/cart/detail.html', {'product': product, 'cart_product_form': cart_product_form})
