from django.http import HttpResponse, JsonResponse
from .models import Purchase

def my_view(request):
    purchases = Purchase.objects.all()
    data = {'purchases': list(purchases.values())}
    return JsonResponse(data)