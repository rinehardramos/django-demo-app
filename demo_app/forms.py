from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Inventory
        fields = ['title', 'description', 'due_date', 'completed']