from django.views.generic import ListView, CreateView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .forms import UserForm
from .models import User
from .serializers import UserSerializer


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail_view.html'


class UserListView(ListView):
    model = User
    template_name = 'user_list_view.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_create_view.html'
    success_url = '/user'


class UserPagination(PageNumberPagination):
    page_size = 10


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    ordering = ['id']
    pagination_class = UserPagination
    filterset_fields = ['id', 'first_name', 'last_name', 'age']
    search_fields = ['id', 'first_name', 'last_name', 'age']
