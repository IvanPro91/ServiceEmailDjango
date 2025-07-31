from django.contrib.auth.views import LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import login_user

app_name = UserConfig.name

urlpatterns = [
    path("", login_user, name="auth"),
    path("logout/", LogoutView.as_view(), name="logout"),
]