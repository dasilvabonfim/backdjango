
from django.urls import path
from .views import index

app_name = 'pizzas'

urlpatterns = [
    path('', index, name='index')
]
