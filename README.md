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

- Created test cases to test all the API endpoints ([tests.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/tests.py)).

- # Invoice Project

## Overview

This project implements a Django application for managing invoices and their details through a RESTful API. The API supports various HTTP methods (GET, POST, PUT, DELETE) for both invoices and their associated details.

## Project Structure

- **Models**: Two Django models have been created to represent invoices and their details. The models are defined in [models.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/models.py).

  - Invoice Model Fields:
    - date
    - customer_name

  - InvoiceDetail Model Fields:
    - invoice (ForeignKey)
    - description
    - quantity
    - unit_price
    - price

- **Serializers and Views**: Serializers and views have been implemented for both models. The code is organized in [serializers.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/serializers.py) and [views.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/views.py).

- **API Endpoints**:
  - `/invoices/`: Handles CRUD operations for invoices.
  - `/invoices/<int:pk>/`: Handles CRUD operations for a specific invoice identified by its primary key.

- **API Payload**:
  - The API accepts invoice details in the payload and creates/updates the associated invoice details accordingly.

- **Tests**: Test cases have been created to ensure the functionality of all API endpoints. The test code can be found in [tests.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/tests.py).

## API Examples

- **Create Invoice Without Details**
  ```json
  POST /invoices/
  {
      "date": "2023-01-01",
      "customer_name": "John Doe"
  }

