from django import forms
from django.contrib.auth import get_user_model

from catalog.models import Tea


class TeaSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class TeaForm(forms.ModelForm):
    supplier = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Tea
        fields = ["name", "price", "harvest_year", "category", "province", "supplier"]



class SupplierSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by last name"
            }
        )
    )
