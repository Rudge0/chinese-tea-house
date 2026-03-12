from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Tea, Supplier, Province, TeaCategory


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


class SupplierCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Supplier
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "website",)


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = "__all__"