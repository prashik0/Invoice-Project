Project Details
Created a single url /invoices/

/invoices/ <br>
/invoices/<int:pk>/

- Created two Django models as per details provided viz. Invoice and InvoiceDetail. ([models.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/models.py))
  - Invoice model fields -> date, customer_name.
  - InvoiceDetail model fields -> invoice (ForeignKey), description, quantity, unit_price, price.
    
- Created Serializers and Views. ([serializers.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/serializers.py), [views.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/views.py))
  
- Created APIs using Django Rest Framework for all the HTTP methods (GET, POST, PUT, DELETE) for the invoice models. 
- The API also accept invoice_details in the payload and create/update the associated invoice details too
- <img width="989" alt="image" src="https://github.com/prashik0/Invoice-Project/assets/88423828/b70ea259-884b-4e12-bcec-a2cfd7b65f49">

- Created test cases to test all the API endpoints [tests.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/tests.py).
