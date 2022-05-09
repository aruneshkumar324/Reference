from django.urls import path
from .views import *


app_name = 'cars'


urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('delete/<int:id>/', delete_view, name='delete_entry'),
]
