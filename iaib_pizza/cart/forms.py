from django import forms

class CartAddProductForm(forms.Form):
    quantity = 1
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartMinusProductForm(forms.Form):
    quantity = 1
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"youremail@example.com"}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ehitajate tee 5-21"}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"37254937933"}))
    city = forms.NullBooleanField(widget=forms.NullBooleanSelect(attrs={"class":"custom-select d-block w-100"}))
    zip = forms.CharField(max_length=5, widget=forms.TextInput(attrs={"class":"form-control"}))
    radio_choices = (
        ("pick_up", 'Pick up on the spot'),
        ("home", 'Delivery to home'),
    )
    delivery_method = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class":"custom-radio"}), choices=radio_choices)
    card_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    card_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
    expiration = forms.CharField(max_length=5, widget=forms.TextInput(attrs={"class":"form-control"}))
    cvv = forms.CharField(max_length=4, widget=forms.TextInput(attrs={"class":"form-control"}))
