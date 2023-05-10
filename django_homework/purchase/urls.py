from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView, PurchaseViewSet

urlpatterns = [
    path('list', PurchaseListView.as_view(), name='purchase'),
    path('<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('add', PurchaseCreateView.as_view(), name='purchase-create'),
]

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls
