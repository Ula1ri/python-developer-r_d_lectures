from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path('', UserListView.as_view(template_name='user_list_view.html'), name='user-list'),
    path('<int:pk>', UserDetailView.as_view(template_name='user_detail_view.html'), name='user-detail'),
    path('add', UserCreateView.as_view(template_name='user_create_view.html'), name='user-create'),
]