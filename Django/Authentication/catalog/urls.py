from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('add_book/', BookCreateView.as_view(), name='add_book'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('my_view/', my_view, name="my_view"),
    path('signup/', CreateNewUserView.as_view(), name='signup'),
    path('profile/', CheckedOutBookByUserView.as_view(), name='profile'),
]
