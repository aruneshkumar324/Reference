from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Genre, Language, Book, BookInstance, Author


def index(request):

    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        "num_books": num_books,
        "num_instance": num_instance,
        "num_instance_available": num_instance_available,
    }

    return render(request, 'catalog/index.html', context)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'

    # success_url = reverse_lazy('catalog:index')


class BookDetail(DetailView):
    model = Book



@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')


# add new user
class CreateNewUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'catalog/signup.html'
    success_url = reverse_lazy('login')


class CheckedOutBookByUserView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
    