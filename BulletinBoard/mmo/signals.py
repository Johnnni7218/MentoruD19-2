from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, send_mass_mail
from .models import Feedback, Post


@receiver(post_save, sender=Feedback)
def feedback_save(sender, instance, **kwargs):
    post_user_email = instance.post.user.email
    send_mail(
        subject='Новый отзыв',
        message='На Ваше объявление оставлен отзыв',
        from_email='Maclac1267@yandex.ru',
        recipient_list=[post_user_email],
    )

