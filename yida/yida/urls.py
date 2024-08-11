from django.contrib import admin
from django.urls import path
from .api import api

urlpatterns = [
    path("yida/", admin.site.urls),
    path("api/", api.urls),
]