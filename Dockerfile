FROM python:3.12

WORKDIR /code

RUN pip install Django

COPY . /code/

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate

RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
