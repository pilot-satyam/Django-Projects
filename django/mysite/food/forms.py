from django import forms
from .models import Item 

class ItemForm(forms.ModelForm):
    class Meta:  #for the form containing which specific fields
        model = Item
        fields = ['item_name','item_desc','item_price','item_image']