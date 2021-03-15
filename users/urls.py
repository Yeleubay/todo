from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.logout, name='logout'),
]
