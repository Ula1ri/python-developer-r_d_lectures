from django.http import HttpResponse, JsonResponse
from .models import Book


def my_view(request):
    books = Book.objects.all()
    data = {'books': list(books.values())}
    return JsonResponse(data)