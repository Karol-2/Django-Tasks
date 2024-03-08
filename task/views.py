from rest_framework import generics
from .permissions import ReadOnlyOrAuthenticated

from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [ReadOnlyOrAuthenticated]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [ReadOnlyOrAuthenticated]


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ReadOnlyOrAuthenticated]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ReadOnlyOrAuthenticated]

