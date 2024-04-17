from django.urls import path
from . import views

app_name = 'r1code'
urlpatterns = [
    path('', views.index, name='index'),
]