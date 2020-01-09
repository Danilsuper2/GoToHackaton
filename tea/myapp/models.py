from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    house = models.IntegerField()
    course = models.CharField(max_length=50)
    candle = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tea(models.Model):
    user_1 = models.CharField(max_length=50)
    user_2 = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return '{}, вместе в {}, в {} в {}'.format(self.user_1, self.user_2, self.place, 'Дата:Время')
