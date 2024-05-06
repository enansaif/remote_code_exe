from django.urls import path
from . import views

app_name = 'r1code'
urlpatterns = [
    path('', views.index, name='index'),
    path('execute_code', views.execute_code, name='execute_code'),
]