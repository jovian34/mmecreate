from django.shortcuts import redirect
import os


def home(request):
    site_is_under_construction = int(os.environ.get("CONSTRUCTION"))
    if site_is_under_construction:
        return redirect("mmestore/construction", request)
    else:
        return redirect("/mmestore", request)
