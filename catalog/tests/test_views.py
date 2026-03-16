from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from ..models import TeaCategory

TEA_CATEGORY_URL = reverse("catalog:tea-category-list")


class PublicTeaCategoryTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TEA_CATEGORY_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTeaCategoryTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
        )
        self.client.force_login(self.user)

    def test_retrieve_tea_categories(self):
        TeaCategory.objects.create(name="pu ehr")
        TeaCategory.objects.create(name="mej")
        res = self.client.get(TEA_CATEGORY_URL)

        self.assertEqual(res.status_code, 200)
        tea_categories = TeaCategory.objects.all()
        self.assertEqual(
            list(res.context["tea_categories_list"]),
            list(tea_categories)
        )
        self.assertTemplateUsed(res, "catalog/tea_category_list.html")


class PrivateSupplierTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )

        self.client.force_login(self.user)

    def test_create_supplier(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "Test last",
            "website": "https://www.google.com",
        }

        self.client.post(reverse("catalog:supplier-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.website, form_data["website"])
