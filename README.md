# Task app
It's a simple django app with api and admin panel. Created with two models - Task and Category.

## Endpoints

- http://127.0.0.1:8000/api/categories - api for categories CRUD
- http://127.0.0.1:8000/api/tasks - api for tasks CRUD
- http://127.0.0.1:8000/admin/ - admin panel
## Postman Requests
Postman example requests are stored in **Django Tasks.postman_collection.json**

## Authentication
Dockerfile should create superuser with:
- username: admin
- password: admin

This account is used to authenticate api CUD requests in my postman request collection.

## Dockerization
1. Create Image
     ```shell
     docker build -t django-tasks .
     ```
2. Create Docker container
   ```shell
   docker run -p 8000:8000 django-tasks
     ```