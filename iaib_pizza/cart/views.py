import datetime
import random

from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pizza.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartMinusProductForm, CheckoutForm
from coupons.forms import CouponApplyFrom
from pizza.views import send_email
from .models import Sales, SalesWithoutDiscount, DiscountSales, OrderInfo


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
    coupon_apply_form = CouponApplyFrom()
    return render(request, 'cart/detail.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})


def checkout(request):
    cart = Cart(request)
    checkout_form = CheckoutForm(request.POST or None)
    if checkout_form.is_valid():
        cd = checkout_form.cleaned_data
        discount = cart.coupon.discount if cart.coupon else None
        order_number = random.randint(0, 999)

        send_message_about_order(cd, cart, order_number)
        fill_order_info(cd, cart, discount)
        fill_sales(cart, discount)

        cart.clear()

    return render(request, 'cart/checkout.html', {'cart': cart, 'checkout_form': checkout_form})


def send_message_about_order(cd, cart, order_number):
    date = datetime.datetime.now()
    now = date.strftime("%Y/%m/%d %H:%M")
    order_time_home = date + datetime.timedelta(minutes=50)
    order_time_home = order_time_home.strftime("%H:%M")
    message = f'Dear {cd["first_name"]},\nThank you for your order!\n\n'
    message += f'Date:  {now}\n\n'
    message += f'Estimated Delivery Time: {order_time_home}\n\n'
    message += f'Order number:  {order_number}.\n\n'
    message += f'Order price:  {cart.get_total_price_after_discount()} €.'
    send_email(cd['email'], message)


def fill_order_info(cd, cart, discount):
    city = 'Tallinn' if cd['city'] is True else None
    amount = [str(q['quantity']) for q in list(cart.cart.values())]
    phone_number = cd['phone_number'].replace('+', '')

    order_info = OrderInfo(name=f'{cd["first_name"]} {cd["last_name"]}', email=cd['email'],
                           city=city, zip=cd['zip'], phone_number=phone_number,
                           discount=discount, products=", ".join(list(cart.cart.keys())), amount=", ".join(amount))

    order_info.save()


def fill_sales(cart, discount):
    for id, q in cart.cart.items():
        item = Sales.objects.filter(product_id=int(id))
        item.update(sold = F('sold') + q['quantity'])
        item.update(income = F('income') + (q['quantity'] * float(q['price'])))
        if discount:
            item = DiscountSales.objects.filter(product_id=int(id), discount=int(discount))
            item.update(sold=F('sold') + q['quantity'])
            item.update(income=F('income') + (q['quantity'] * float(q['price']) * int(discount)))
        else:
            item = SalesWithoutDiscount.objects.filter(product_id=int(id))
            item.update(sold=F('sold') + q['quantity'])
            item.update(income=F('income') + (q['quantity'] * float(q['price'])))
