from django.contrib import auth
from django.http import HttpRequest
from django.shortcuts import render
from django.views.defaults import permission_denied


def login_user(request: HttpRequest):
    chk_post = request.POST
    if chk_post:
        email = chk_post.get("email-username")
        password = chk_post.get("password")
        user = auth.authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user)
        else:
            return permission_denied(request, ValueError)
    return render(request, "recipients.html")