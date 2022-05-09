from pyexpat import model
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .form import ContactForm
from .models import Teacher


class HomeView(TemplateView):
    template_name = 'classroom/index.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher

    # fields = ['first_name', 'last_name']
    fields = '__all__'

    success_url = reverse_lazy('classroom:teacher_list')


class TeacherListView(ListView):
    # required
    model = Teacher

    # not required 
    # defualt   =   Teacher.objects.all()
    queryset = Teacher.objects.order_by('first_name')

    # not required
    # if you want change 'object_list' for loop
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher

    fields = '__all__'

    success_url = reverse_lazy('classroom:teacher_list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success_url = '/classroom/thank_you/'
    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)