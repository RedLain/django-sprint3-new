from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogModel(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Post(BlogModel):
    title = models.CharField('Название', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateField('Дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post',
        verbose_name='Автор'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Город'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категории'
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'


class Category(BlogModel):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(BlogModel):
    name = models.CharField('Название', max_length=256)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'Города'




