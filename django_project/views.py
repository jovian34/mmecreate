from django.shortcuts import redirect
import os


def home(request):
    return redirect("/mmestore", request)
