from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('create-account/', views.create_account, name='create_account'),
]