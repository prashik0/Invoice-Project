# Invoice Project

## Overview

This project implements a Django application for managing invoices and their details through a RESTful API. The API supports various HTTP methods (GET, POST, PUT, DELETE) for both invoices and their associated details.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <project_directory>

1. **Create a Virtual Environment::**

   ```bash
   virtualenv env

1. **Activate the Virtual Environment:**

   ```bash
   source env/bin/activate

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

1. **Create Database Tables:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate

1. **Run the Development Server:**

   ```bash
   python manage.py runserver
   
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
  - <img width="989" alt="image" src="https://github.com/prashik0/Invoice-Project/assets/88423828/b70ea259-884b-4e12-bcec-a2cfd7b65f49">

- **Tests**: Test cases have been created to ensure the functionality of all API endpoints. The test code can be found in [tests.py](https://github.com/prashik0/Invoice-Project/blob/main/core/invoice/tests.py).

## API Examples

- **Create Invoice**
  ```json
  POST /invoices/
- **Get Invoices**
  ```json
  GET /invoices/
- **Update Invoice**
  ```json
  PUT /invoices/<int:pk>/
- **Delete Invoice**
  ```json
  DELETE /invoices/<int:pk>/ 
