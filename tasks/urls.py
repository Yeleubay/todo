from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tasks_list, name='tasks_list'),
    path('<str:pk>/', views.get_task, name='task'),
    path('<str:pk>/execute/', views.execute)

]
