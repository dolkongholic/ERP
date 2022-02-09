import datetime
from django import forms
from django.db.models import Q
from django.contrib import messages
from . import models


class productForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = (
            "product_code",
            "product_name_in",
            "product_name_out",
            "product_size",
            "product_count",
            "product_init_count",
            "product_init_price_in",
            "product_vat_in",
            "product_init_price_out",
            "product_vat_out",
            "product_group",
        )

class companiesForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = (
            "code",
            "name",
            "owner",
            "keyperson",
            "type",
            "type_2",
            "tel",
            "phone",
            "email",
            "address",
            "bank",
            "bank_address",
            "group",
        )

class companiesGroupForm(forms.ModelForm):
    class Meta:
        model = models.Company_group
        fields = (
            "name",
        )

        
        
        