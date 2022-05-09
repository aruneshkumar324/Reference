from django.urls import path
from .views import *


urlpatterns = [
    path('', office_view, name='office_view')
]
