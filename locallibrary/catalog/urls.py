from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Make sure your views are correctly mapped
]
