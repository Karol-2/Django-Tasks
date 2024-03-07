from django.contrib import admin
from .models import Category
from .models import Task

# Register your models here.
admin.site.register(Category)
admin.site.register(Task)
