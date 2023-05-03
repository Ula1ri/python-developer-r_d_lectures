from django.http import HttpResponse, JsonResponse
from .models import User

def my_view(request):
    users = User.objects.all()
    data = {'users': list(users.values())}
    return JsonResponse(data)