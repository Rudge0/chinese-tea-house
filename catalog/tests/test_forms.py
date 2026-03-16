from django.test import TestCase

from catalog.forms import SupplierCreationForm


class FormsTests(TestCase):
    def test_supplier_creation_form_with_website_first_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Supplier1324",
            "last_name": "Supplier1324",
            "website": "https://www.google.com",
        }
        form = SupplierCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
