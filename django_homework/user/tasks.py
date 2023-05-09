from celery import shared_task
from .models import User


@shared_task
def print_text():
    print('My task!')

@shared_task
def count_purchases(user_id):
    user = User.objects.get(id=user_id)
    purchase_count = user.purchase_set.count()
    print(f'Користувач {user.last_name} зробив {purchase_count} покупок.')

@shared_task
def print_users_count():
    user_count = User.objects.count()
    print(f" User count: {user_count}")

