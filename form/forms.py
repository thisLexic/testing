from .models import Entry, Product, DailyCash
from django import forms
from django.utils.translation import gettext_lazy
from django.forms import modelformset_factory



class CreateEntryForm(forms.ModelForm):
    # product_number_set = modelformset_factory(
    #     model=Entry, 
    #     fields=("product_number",), 
    #     extra= c,
    #     labels={"product_number":""},
    #     min_num=c,
    #     validate_min=True,
    #     )(queryset=Entry.objects.none())
    class Meta:
        model = Entry
        fields = ('branch', 'date')
        labels = {
            'date': gettext_lazy('Entry Date'),
            'branch': gettext_lazy('Branch'),
        }
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'})
        }


c = Product.objects.all().count()
products = modelformset_factory(
        model=Entry, 
        fields=("product_number",), 
        extra= c,
        labels={"product_number":""},
        )
ProductNumberFormSet = products(queryset=Entry.objects.none())

class CreateDailyCashForm(forms.ModelForm):
    class Meta:
        model = DailyCash
        fields = ('actual_income',)
        labels = {
            'actual_income': gettext_lazy('Cash in Caja'),
        }