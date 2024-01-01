Project Details
Created a single url /invoices/

/invoices/
/invoices/<int:pk>/

- Created two Django models as per details provided viz. Invoice and InvoiceDetail. ([models.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/models.py))
  - Invoice model fields -> date, customer_name.
  - InvoiceDetail model fields -> invoice (ForeignKey), description, quantity, unit_price, price.
- Created Serializers and Views .
- Created APIs using Django Rest Framework for all the HTTP methods for the invoice models. 
- The API should also accept invoice_details in the payload and create/update the associated invoice details too 
- Created test cases to test all the API endpoints.
