# api/urls.py

from django.urls import path
from .views import RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # ✅ Register (Doctor/Patient)
    path("register/", RegisterView.as_view(), name="register"),

    # ✅ Login (JWT Token generate)
    path("login/", TokenObtainPairView.as_view(), name="login"),

    # ✅ Refresh Token
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ✅ Current User Info
    path("me/", UserDetailView.as_view(), name="user_detail"),
]
