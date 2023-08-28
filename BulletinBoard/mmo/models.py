from django.contrib.auth.models import User
from django.db import models

tanks = 'TNK'
hils = 'HIL'
dd = 'DD'
merchants = 'MCH'
guild_masters = 'GMA'
quest_givers = 'QMA'
blacksmiths = 'BLM'
tanners = 'TAN'
potion_makers = 'PMK'
spell_masters = 'SMA'

CATEGORY = [
    (tanks, 'Танки'),
    (hils, 'Хилы'),
    (dd, 'ДД'),
    (merchants, 'Торговцы'),
    (guild_masters, 'Гилдмастеры'),
    (quest_givers, 'Квестгиверы'),
    (blacksmiths, 'Кузнецы'),
    (tanners, 'Кожевники'),
    (potion_makers, 'Зельевары'),
    (spell_masters, 'Мастера заклинаний'),
]


class Post(models.Model):
    name_post = models.CharField(max_length=255)
    body_post = models.TextField()
    category = models.CharField(max_length=3, choices=CATEGORY, default=tanks)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #
    # def __str__(self):
    #     return f'{self.name_post}: {self.body_post[:40]}'


class Feedback(models.Model):
    body_feedback = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)



