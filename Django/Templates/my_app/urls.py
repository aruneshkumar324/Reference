from django.urls import path
from .views import *

app_name = 'my_app'

urlpatterns = [
    path('', home, name='home'),
    path('variables/', variable_view, name='variables'),
    path('example/', example_view, name='example'),
]
