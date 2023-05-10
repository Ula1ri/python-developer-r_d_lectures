from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListView, BookDetailView, BookCreateView, BookViewSet

urlpatterns = [
    path('list', BookListView.as_view(), name='book'),
    path('<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('add', BookCreateView.as_view(), name='book-create'),
]

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns += router.urls