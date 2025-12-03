from django import forms
from products.models import Product
from .models import Order

class AddToOrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1, initial=1)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'status', ]
