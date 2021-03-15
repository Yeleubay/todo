from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('all/', views.get_tasks_list, name='tasks_list'),
    path('<str:pk>/', views.get_task, name='task'),
    path('<str:pk>/update/', views.update_task, name='update_task'),
    path('<str:pk>/delete/', views.delete_task, name='delete_task'),
    path('<str:pk>/execute/', views.execute, name='execute_task'),
]
