from django.urls import path
from .views import TaskList, TaskDetail, CategoryList, CategoryDetail

urlpatterns =  [
    path('task/', TaskList.as_view()),
    path('task/<int:pk>/', TaskDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
]