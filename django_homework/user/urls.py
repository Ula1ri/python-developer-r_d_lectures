from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserListView, UserDetailView, UserCreateView, UserViewSet

urlpatterns = [
    path('list', UserListView.as_view(template_name='user_list_view.html'), name='user-list'),
    path('<int:pk>', UserDetailView.as_view(template_name='user_detail_view.html'), name='user-detail'),
    path('add', UserCreateView.as_view(template_name='user_create_view.html'), name='user-create'),
]

router = SimpleRouter()
router.register('', UserViewSet)


urlpatterns += router.urls
