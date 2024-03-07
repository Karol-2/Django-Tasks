from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)


class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    completed = models.BooleanField()
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)


# python manage.py makemigrations
# python manage.py migrate
