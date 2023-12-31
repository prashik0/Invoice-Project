from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail
from datetime import datetime


class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice_data = {"date": "2023-01-01", "customer_name": "Prashik Raut"}
        self.invoice = Invoice.objects.create(**self.invoice_data)

        self.invoice_detail_data = {
            "invoice": self.invoice.id,
            "description": "Item 1",
            "quantity": 2,
            "unit_price": 10.0,
            "price": 20.0,
        }

    def test_create_invoice_without_details(self):
        data = {
            "date": "2023-01-01",
            "customer_name": "Prashik Raut",
            "details": [],
        }
        self.create_invoice_data(data)

    def test_create_invoice_with_details(self):
        data = {
            "date": "2023-01-01",
            "customer_name": "Prashik Raut",
            "details": [self.invoice_detail_data],
        }
        self.create_invoice_data(data)
        self.assertEqual(InvoiceDetail.objects.count(), 1)

    def create_invoice_data(self, data):
        response = self.client.post("/invoices/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)

    def test_update_invoice(self):
        updated_data = {
            "date": "2023-01-02",
            "customer_name": "Updated Customer",
            "details": [self.invoice_detail_data],
        }
        response = self.client.put(
            f"/invoices/{self.invoice.pk}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.assertEqual(
            self.invoice.date,
            datetime.strptime(updated_data["date"], "%Y-%m-%d").date(),
        )
        self.assertEqual(self.invoice.customer_name, updated_data["customer_name"])

    def test_get_invoice_list(self):
        response = self.client.get("/invoices/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data), 1
        )  # Assuming there is an initial invoice created

    def test_get_invoice_detail(self):
        response = self.client.get(f"/invoices/{self.invoice.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["customer_name"], self.invoice_data["customer_name"]
        )

    def test_delete_invoice(self):
        response = self.client.delete(f"/invoices/{self.invoice.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)

    def test_create_invoice_with_invalid_data(self):
        invalid_data = {"date": "invalid-date", "customer_name": ""}
        response = self.client.post("/invoices/", invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invoice_with_invalid_data(self):
        invalid_data = {"date": "invalid-date", "customer_name": ""}
        response = self.client.put(
            f"/invoices/{self.invoice.pk}/", invalid_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
