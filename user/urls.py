from django.urls import path

from user.apps import UserConfig
from user.views import (chk_token, form_auth, form_reg, login_user,
                        logout_user, registration)

app_name = UserConfig.name

urlpatterns = [
    path("", login_user, name="auth"),
    path("auth/", form_auth, name="form_auth"),
    path("reg/", form_reg, name="form_reg"),
    path("registration/", registration, name="registration"),
    path("logout/", logout_user, name="logout"),
    path("token/<str:token>", chk_token, name="token"),
]
