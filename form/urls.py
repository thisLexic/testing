from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "form"

urlpatterns = [
    path('', views.create_sold, name="create"),
    path('inventory/', views.create_inventory, name="inventory"),
]