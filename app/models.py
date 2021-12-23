"""
Definition of models.
"""

from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User

# Модель данных блока
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = "temp.jpg", verbose_name = "Путь к картинке")

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
        ordering = ["-posted"]
        verbose_name = "статья блога"
        verbose_name_plural = "статья блога"

admin.site.register(Blog)

class Pizza(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Название")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Добавлен")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = "temp.jpg", verbose_name = "Путь к картинке")

    def get_absolute_url(self):
        return reverse("pizzapost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "pizzaposts"
        ordering = ["-posted"]
        verbose_name = "продукт каталога (Пицца)"
        verbose_name_plural = "продукт каталога (Пицца)"

admin.site.register(Pizza)

class Sup(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Название")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Добавлен")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = "temp.jpg", verbose_name = "Путь к картинке")

    def get_absolute_url(self):
        return reverse("suppost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "supposts"
        ordering = ["-posted"]
        verbose_name = "продукт каталога (Суп)"
        verbose_name_plural = "продукт каталога (Суп)"

admin.site.register(Sup)

class Roll(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Название")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Добавлен")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = "temp.jpg", verbose_name = "Путь к картинке")

    def get_absolute_url(self):
        return reverse("rollpost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "rollposts"
        ordering = ["-posted"]
        verbose_name = "продукт каталога (Ролл)"
        verbose_name_plural = "продукт каталога (Ролл)"

admin.site.register(Roll)

class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")

    def __str__(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии к статьям блога"
        ordering = ["-date"]

admin.site.register(Comment)

class CommentZ(models.Model):
    name = models.CharField(max_length = 100, default = '', verbose_name = "Ваше имя")
    phone = models.CharField(max_length = 100, default = '', verbose_name = "Ваш телефон")
    address = models.CharField(max_length = 100, default = '', verbose_name = "Адрес доставки")
    text = models.TextField(verbose_name = "Напишите, что вы хотите заказать, и ваши личные пожелания к заказу")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")

    def __str__(self):
        return 'Заказ %s %s' % (self.author, self.date)

    class Meta:
        db_table = "CommentsZ"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы клиентов"
        ordering = ["-date"]

admin.site.register(CommentZ)