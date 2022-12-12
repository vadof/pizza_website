from django import forms

class CartAddProductForm(forms.Form):
    quantity = 1
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartMinusProductForm(forms.Form):
    quantity = 1
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)