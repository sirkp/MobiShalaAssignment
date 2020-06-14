# MobishalaAssignment
An api for user login, register, product list and product rating endpoint. **TokenAuthentication** is used for authenticaton. **Sqlite 3.31** is used as database.

### Frameworks used
- django 3.0
- django rest framework 3.11

### Setup instruction
- conda create --name env python=3.7
- conda install -v django
- pip install djangorestframework
- conda activate env
- python manage.py createsuperuser
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

### Endpoints
- base_url/api/register/
- base_url/api/login/
- base_url/api/products/
- base_url/api/rate/

### Postman Collection
- [Collection](https://www.getpostman.com/collections/1672827fbd62b19d70e1)
