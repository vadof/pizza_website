from django import forms

class CartAddProductForm(forms.Form):
    quantity = 1
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartMinusProductForm(forms.Form):
    quantity = 1
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    address = forms.CharField(max_length=50)
    city = forms.NullBooleanField()
    zip = forms.IntegerField()
    delivery_method = forms.BooleanField()
    card_name = forms.CharField(max_length=100)
    card_number = forms.IntegerField()
    expiration = forms.CharField(max_length=100)
    cvv = forms.IntegerField()
