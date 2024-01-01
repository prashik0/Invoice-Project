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

### Test Cases:

1. **Without Date:**
   - Request:
     ```json
     {}
     ```
   - Response:
     ```json
     {
       "date": [
         "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
       ]
     }
     ```

2. **Invalid Date:**
   - Request:
     ```json
     {
       "date": "invalid-date"
     }
     ```
   - Response:
     ```json
     {
       "date": [
         "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
       ]
     }
     ```

3. **Without Customer Name:**
   - Request:
     ```json
     {
       "date": "2023-01-01"
     }
     ```
   - Response:
     ```json
     {
       "customer_name": [
         "This field may not be blank."
       ]
     }
     ```

4. **Remove "Date" or "Customer Name" Key:**
   - Request:
     ```json
     {
       "customer_name": "John Doe"
     }
     ```
   - Response:
     ```json
     {
       "date": [
         "This field is required."
       ]
     }
     ```

5. **Optional "Details" Field (Remove It):**
   - Request:
     ```json
     {
       "date": "2023-12-20",
       "customer_name": "John Doe"
     }
     ```
   - Response:
     ```json
     {
       "id": 27,
       "date": "2023-12-20",
       "customer_name": "John Doe",
       "details": []
     }
     ```

6. **Keep "Details" Key, No Data:**
   - Request:
     ```json
     {
       "date": "2023-12-20",
       "customer_name": "John Doe",
       "details": []
     }
     ```
   - Response:
     ```json
     {
       "id": 28,
       "date": "2023-12-20",
       "customer_name": "John Doe",
       "details": []
     }
     ```

7. **Missing Key in "Details" (e.g., "Price"):**
   - Request:
     ```json
     {
       "date": "2023-12-20",
       "customer_name": "John Doe",
       "details": [
         {
           "quantity": 2,
           "unit_price": 10.0
         }
       ]
     }
     ```
   - Response:
     ```json
     {
       "details": [
         {
           "price": [
             "This field is required."
           ]
         }
       ]
     }
     ```

8. **Invalid Unit Price in "Details":**
   - Request:
     ```json
     {
       "date": "2023-12-20",
       "customer_name": "John Doe",
       "details": [
         {
           "quantity": 2,
           "unit_price": "11a.40",
           "price": 22.0
         }
       ]
     }
     ```
   - Response:
     ```json
     {
       "details": [
         {
           "unit_price": [
             "A valid number is required."
           ]
         }
       ]
     }
     ```


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
