from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Введите жанр книги', verbose_name='Жанр книги')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text='Введите язык книги', verbose_name='Язык книги')

    def __str__(self):
        return self.name

