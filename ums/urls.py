from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # Loginn app
    path('accounts/', include('accounts.urls')),

    # User Dashboards
    path('dashboards/', include('dashboards.superuser.urls')),
]
