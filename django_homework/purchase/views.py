from .models import Purchase
from django.views.generic import ListView, CreateView, DetailView
from .forms import PurchaseForm


class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = '/purchase'
