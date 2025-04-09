from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list_create, name = 'task_list_create'),
    path('task/<int:pk>/', views.task_detail, name = 'task_detail' ),
]
