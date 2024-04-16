from django.contrib.auth import get_user_model

from django.db import models

from core.models import IsPublishedCreatedAt

from blog.myconst import CHAR_LENGTH

User = get_user_model()


class Category(IsPublishedCreatedAt):
    title = models.CharField(max_length=CHAR_LENGTH, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True,
                            verbose_name='Идентификатор',
                            help_text='Идентификатор страницы для URL;'
                            ' разрешены символы латиницы, цифры, дефис'
                            ' и подчёркивание.')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:20]


class Location(IsPublishedCreatedAt):
    name = models.CharField(max_length=CHAR_LENGTH, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:20]


class Post(IsPublishedCreatedAt):
    title = models.CharField(max_length=CHAR_LENGTH, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    help_text='Если установить дату и время в'
                                    ' будущем — можно делать отложенные'
                                    ' публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Местоположение',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Категория',
        null=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title[:20]
