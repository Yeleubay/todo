from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_create, name='task_list_create'),
    path('<str:pk>/', views.task_manipulation, name='task_manipulation'),
    path('<str:pk>/execute/', views.execute, name='execute_task'),
]
