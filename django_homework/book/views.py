from .models import Book
from django.views.generic import ListView, CreateView, DetailView
from .forms import BookForm


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    success_url = '/book'
    form_class = BookForm

