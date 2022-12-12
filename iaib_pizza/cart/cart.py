from decimal import Decimal
from django.conf import settings
from pizza.models import Product
from coupons.models import Coupon

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupons = ['OPEN10', 'NICE20', 'TdfspUFDSO']
        self.coupon_id = self.session.get('coupon_id')

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def minus(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id in self.cart:
            if update_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] -= quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def apply_discount(self, coupon):
        if coupon in self.coupons:
            self.discount = True
            self.coupons.remove(coupon)
            self.save()

    def get_total_price(self):
        total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        return total

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return round((self.coupon.discount / Decimal('100')) * self.get_total_price(), 2)
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

    def get_total_price_with_delivery(self):
        return self.get_total_price_after_discount() + 2

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
