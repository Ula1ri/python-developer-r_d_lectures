from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='book'),
    path('<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('add', BookCreateView.as_view(), name='book-create'),
]
