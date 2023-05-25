from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts_auth import views
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt import views as jwt_views


accounts_urlpatterns = [
    path('auth/v1/users/signup/', views.UserCreateView.as_view(), name='user_register'),
    path('auth/v1/api/token/verify/',TokenVerifyView.as_view(), name='token_verify'),
    path('auth/v1/login/', views.UserTokenObtainPairView.as_view(), name='login'),
    path('auth/v1/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('auth/v1/home', views.HomeView.as_view(), name='home'),
]

