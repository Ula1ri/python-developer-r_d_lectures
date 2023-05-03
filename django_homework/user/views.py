from .models import User
from django.views.generic import ListView, CreateView, DetailView
from .forms import UserForm


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
