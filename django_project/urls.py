from django.contrib import admin
from django.urls import include, path
from . import views

import os

admin_word = os.environ.get("ADMIN_WORD")

urlpatterns = [
    path("", views.home, name="home"),
    path("mmestore/", include("mmestore.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path(f"{admin_word}/", admin.site.urls),
]

admin.site.site_header = "Mmes Creations LLC"
admin.site.site_title = "Mmes Store Inventory"
admin.site.index_title = "Mmes Store Inventory"
