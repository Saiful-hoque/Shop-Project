#  Simple Product API (Django REST Framework)

A clean RESTful API built for a small online shop using **Python**, **Django**, and **Django REST Framework (DRF)**. Visitors can browse available products without authentication, while only authenticated users with valid tokens can create new products.

---

##  Features & Implementation Summary

- **Project & App Structure**: `shop_project` with `products` application.
- **Product Model**: Contains `id` (auto-generated), `name` (max 100 characters), `description`, `price` (decimal, up to 2 decimal places), and `stock` (integer).
- **Custom ModelSerializer**:
  - `id` is read-only.
  - Validates that `name` is not empty.
  - Validates that `price` is strictly greater than zero (`> 0`).
  - Validates that `stock` is non-negative (`>= 0`).
- **Endpoints (`GET` & `POST` on `/api/products/`)**:
  - `GET /api/products/`: Publicly accessible, products ordered by `id`, returns paginated response.
  - `POST /api/products/`: Protected endpoint, requires Token Authentication, returns `201 Created` with generated `id`.
- **Token Authentication & Permissions**:
  - Built-in `TokenAuthentication`.
  - `IsAuthenticatedOrReadOnly` permission class.
  - Token acquisition endpoint at `/api/api-token-auth/`.
- **Pagination**: Configured `PAGE_SIZE = 5` so adding 6 products shows the 6th product on page 2 (`?page=2`).

---

##  Tech Stack

- Python 3.x
- Django 4.x / 5.x
- Django REST Framework (DRF)
- SQLite3

---

##  How to Setup & Run Locally

### 1. Clone repository & create virtual environment
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd shop_project

# Create virtual environment
python -m venv env

# Activate:
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run database migrations
```bash
python manage.py makemigrations products
python manage.py migrate
```

### 4. Create a test user & authentication token
Run Django shell:
```bash
python manage.py shell
```
Inside the interactive shell:
```python
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.create_user(username='testuser', password='password123')
token = Token.objects.create(user=user)
print("Token Key:", token.key)
exit()
```

### 5. Start the development server
```bash
python manage.py runserver
```
API root URL: `http://127.0.0.1:8000/api/products/`

---

##  API Endpoints & Postman Testing Guide

### 1. View Products (Public)
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/products/`
- **Header**: None needed
- **Status**: `200 OK`

### 2. Add Product (Authenticated)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/products/`
- **Headers**:
  - `Authorization`: `Token YOUR_TOKEN_KEY`
  - `Content-Type`: `application/json`
- **Body (raw JSON)**:
  ```json
  {
    "name": "Notebook",
    "description": "A notebook with 100 pages.",
    "price": "120.00",
    "stock": 25
  }
  ```
- **Status**: `201 Created`

### 3. Add Product Without Token (Authentication Error)
- **Method**: `POST` without `Authorization` header
- **Status**: `401 Unauthorized`

### 4. Validation Errors (Handled by Serializer)
- Empty name: `{"name": ["Product name cannot be empty."]}`
- Price <= 0: `{"price": ["Price must be greater than zero."]}`
- Stock < 0: `{"stock": ["Stock cannot be negative."]}`

### 5. Page 2 Pagination Test
- Add 6 products using POST.
- Request: `GET http://127.0.0.1:8000/api/products/?page=2`
- Returns only the 6th product.

---

##  Screenshots for Submission Checklist
Save your Postman test results inside `screenshots/`:
1. `1_get_products_public.png` - Successful GET response.
2. `2_post_product_success.png` - Successful 201 Created with Token.
3. `3_auth_error_401.png` - POST attempt without token showing 401 Unauthorized.
4. `4_validation_error.png` - Negative price/stock validation error response.
5. `5_pagination_page_2.png` - GET request to `?page=2` displaying 6th product.

---


