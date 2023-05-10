from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Book
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, CreateView, DetailView
from .forms import BookForm
from .serializers import BookSerializer


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    success_url = '/book'
    form_class = BookForm


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'title', 'author', 'year', 'prise']
    search_fields = ['id', 'date', 'book_id_id', 'user_id_id']
