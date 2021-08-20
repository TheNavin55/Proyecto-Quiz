from django.urls import path
from . import views

app_name='apps.blog'

urlpatterns = [
    path('nosotros/', views.nosotros)
]