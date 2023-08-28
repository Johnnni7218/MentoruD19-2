from celery import shared_task
from django.core.mail import send_mail

from .models import Post


@shared_task
def accept_alert():
    user_mail = Post.user.email
    send_mail(
        subject='Реакция на Ваш отзыв',
        message='Ваш отзыв принят автором объявления',
        from_email='Maclac1267@yandex.ru',
        recipient_list=[user_mail],
    )
