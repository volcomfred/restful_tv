from django.urls import path, include
from shows import views

urlpatterns = [
    path('', views.index),
    path('shows/', include('shows.urls')),
]