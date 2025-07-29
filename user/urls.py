from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def test_view(req):
    return render(req, "auth.html")


urlpatterns = [
    path("", test_view, name="auth"),
]
