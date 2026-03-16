from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test_admin",
        )
        self.client.force_login(self.admin_user)
        self.supplier = get_user_model().objects.create_user(
            username="supplier",
            password="test_supplier",
            website="test_website",
        )

    def test_supplier_website_listed(self):
        """
        Tests that supplier's website is in
        list_display on supplier admin page
        """

        url = reverse("admin:catalog_supplier_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.supplier.website)

    def test_supplier_detail_website_listed(self):
        """
        Tests that supplier`s website is in
        supplier admin detail page
        """

        url = reverse("admin:catalog_supplier_change", args=[self.supplier.id])
        res = self.client.get(url)
        self.assertContains(res, self.supplier.website)
