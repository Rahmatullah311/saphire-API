from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path("tokenshield/token/", UserLoginView.as_view(), name="tokengenerate"),
    path("tokenshield/token/refresh/", TokenRefreshView.as_view(), name="tokenrefresh"),
    path("tokenshield/token/verify/", TokenVerifyView.as_view(), name="tokenverify"),
    path("tokenshield/token/block/", TokenBlacklistView.as_view(), name="tokenblock"),
    path("tokenshield/user/register/", UserRegisterView.as_view(), name="userregister"),
]
