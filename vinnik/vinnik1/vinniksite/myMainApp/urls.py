from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('salary', views.salary_page)
]