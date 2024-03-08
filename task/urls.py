from django.urls import path
from .views import TaskList, TaskDetail, CategoryList, CategoryDetail

urlpatterns =  [
    path('tasks', TaskList.as_view()),
    path('tasks/<int:pk>', TaskDetail.as_view()),
    path('categories', CategoryList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
]