from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail
from datetime import datetime


class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        # Set up initial data for the invoice and its details
        self.invoice_data = {"date": "2023-01-01", "customer_name": "Prashik Raut"}
        self.invoice = Invoice.objects.create(**self.invoice_data)

        self.invoice_detail_data = {
            "invoice": self.invoice.pk,
            "description": "Item 1",
            "quantity": 2,
            "unit_price": 10.0,
            "price": 20.0,
        }

    def test_create_invoice_without_details(self):
        # Test case for creating an invoice without details
        response = self.create_invoice_data(self.invoice_data)

        # Assert that the response status is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the created invoice from the database
        created_invoice = Invoice.objects.get(pk=response.data["id"])

        # Assert that the created invoice data matches the expected data
        self.assertEqual(
            created_invoice.date,
            datetime.strptime(self.invoice_data["date"], "%Y-%m-%d").date(),
        )
        self.assertEqual(
            created_invoice.customer_name, self.invoice_data["customer_name"]
        )

        # Assert that no details are associated with the created invoice
        self.assertEqual(created_invoice.details.count(), 0)

    def test_create_invoice_with_details(self):
        # Test case for creating an invoice with details
        data = {
            "date": "2023-01-01",
            "customer_name": "Prashik Raut",
            "details": [self.invoice_detail_data],
        }
        response = self.create_invoice_data(data)

        # Assert that the response status is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that one InvoiceDetail object is created
        self.assertEqual(InvoiceDetail.objects.count(), 1)

    def create_invoice_data(self, data):
        # Helper method to make a POST request to create an invoice and return the response
        response = self.client.post("/invoices/", data, format="json")

        # Assert that the response status is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the total number of invoices in the database is 2
        self.assertEqual(Invoice.objects.count(), 2)

        return response

    def test_update_invoice(self):
        # Test case for updating an existing invoice
        updated_data = {
            "date": "2023-01-02",
            "customer_name": "Updated Customer",
            "details": [self.invoice_detail_data],
        }
        response = self.client.put(
            f"/invoices/{self.invoice.pk}/", updated_data, format="json"
        )

        # Assert that the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the invoice instance from the database
        self.invoice.refresh_from_db()

        # Assert that the updated invoice data matches the expected data
        self.assertEqual(
            self.invoice.date,
            datetime.strptime(updated_data["date"], "%Y-%m-%d").date(),
        )
        self.assertEqual(self.invoice.customer_name, updated_data["customer_name"])

    def test_get_invoice_list(self):
        # Test case for retrieving a list of invoices
        response = self.client.get("/invoices/")

        # Assert that the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the length of the response data is 1, assuming an initial invoice exists
        self.assertEqual(len(response.data), 1)

    def test_get_invoice_detail(self):
        # Test case for retrieving details of a specific invoice
        response = self.client.get(f"/invoices/{self.invoice.pk}/")

        # Assert that the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the customer_name in the response matches the initial invoice data
        self.assertEqual(
            response.data["customer_name"], self.invoice_data["customer_name"]
        )

    def test_delete_invoice(self):
        # Test case for deleting an existing invoice
        response = self.client.delete(f"/invoices/{self.invoice.pk}/")

        # Assert that the response status is 204 (No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert that there are no invoices in the database after deletion
        self.assertEqual(Invoice.objects.count(), 0)

    def test_create_invoice_with_invalid_data(self):
        # Test case for creating an invoice with invalid data
        invalid_data = {"date": "invalid-date", "customer_name": ""}
        response = self.client.post("/invoices/", invalid_data, format="json")

        # Assert that the response status is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invoice_with_invalid_data(self):
        # Test case for updating an invoice with invalid data
        invalid_data = {"date": "invalid-date", "customer_name": ""}
        response = self.client.put(
            f"/invoices/{self.invoice.pk}/", invalid_data, format="json"
        )

        # Assert that the response status is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
