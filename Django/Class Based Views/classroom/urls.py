from django.urls import path
# from .views import HomeView, ThankYouView, ContactView, TeacherCreateView
from .views import *


app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('teacher/', TeacherCreateView.as_view(), name='teacher'),
    path('list_teacher/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('update_teacher/<int:pk>/', TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>/', TeacherDeleteView.as_view(), name='delete_teacher'),
]