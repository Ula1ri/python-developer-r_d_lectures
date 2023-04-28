from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase'),
    path('<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('add', PurchaseCreateView.as_view(), name='purchase-create'),
]