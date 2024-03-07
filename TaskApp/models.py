from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    completed = models.BooleanField()
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# python manage.py makemigrations
# python manage.py migrate
