from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Purchase
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.viewsets import ModelViewSet
from .forms import PurchaseForm
from .serializers import PurchaseSerializer


class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = '/purchase'


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'date', 'book_id_id', 'user_id_id']
    search_fields = ['id', 'date', 'book_id_id', 'user_id_id']
