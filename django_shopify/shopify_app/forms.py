from django import forms

class ShopLoginForm(forms.Form):
    shop_name = forms.CharField(max_length=200)
