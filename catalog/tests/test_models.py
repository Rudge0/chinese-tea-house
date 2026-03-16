from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import TeaCategory, Tea, Province


class ModelTests(TestCase):
    def test_tea_category_str(self):
        tea_category = TeaCategory.objects.create(name="test")
        self.assertEqual(str(tea_category), tea_category.name)

    def test_supplier_str(self):
        supplier = get_user_model().objects.create(
            first_name="test1",
            last_name="test2",
            username="test_username",
            password="test_password"
        )
        self.assertEqual(str(supplier), f"{supplier.first_name} {supplier.last_name}")

    def test_tea_str(self):
        tea_category = TeaCategory.objects.create(name="test")
        tea_province = Province.objects.create(name="test_province")
        tea = Tea.objects.create(
            name="test",
            price=10.3,
            harvest_year=2013,
            category=tea_category,
            province=tea_province,
        )
        self.assertEqual(
            str(tea),
            f"{tea.name} {tea.category}",
        )

    def test_create_supplier_with_website(self):
        username = "test_username"
        password = "test_password"
        website = "https://www.google.com"
        supplier = get_user_model().objects.create_user(
            first_name="test1",
            last_name="test2",
            username=username,
            password=password,
            website="https://www.google.com",
        )
        self.assertEqual(supplier.username, username)
        self.assertEqual(supplier.website, website)
        self.assertTrue(supplier.check_password(password))
