from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pizza.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartMinusProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, update_quantity=cd['update'])
    return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


@require_POST
def cart_minus(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartMinusProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.minus(product=product, update_quantity=cd['update'])
    return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
