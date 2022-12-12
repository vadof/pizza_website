from django import forms


class CouponApplyFrom(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={"class":"cart_total_promotion_code", "placeholder":"Coupon Code"}))