from django.db import models
from django.contrib.auth.models import User
import os

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    telegram_alias = models.CharField(max_length=30)
    messenger_alias = models.CharField(max_length=30)


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    cover = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    TYPE_CHOICES = [
        (1, 'Action and adventure'),
        (2, 'Art/architecture'),
        (3, 'Autobiography'),
        (4, 'Business/economics'),
        (5, 'Classic'),
        (6, 'Cookbook'),
        (7, 'Dictionary'),
        (8, 'Crime'),
        (9, 'Encyclopedia'),
        (10, 'Drama'),
        (11, 'Guide'),
        (12, 'Fairytale'),
        (13, 'Health/fitness'),
        (14, 'Fantasy'),
        (15, 'History'),
        (16, 'Humor'),
        (17, 'Horror'),
        (18, 'Journal'),
        (19, 'Mystery'),
    ]
    type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
    )

class Interested(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
