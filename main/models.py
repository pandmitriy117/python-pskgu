from django.db import models

class Contact(models.Model):
    def __str__(self):
        return f'#{self.id} {self.name}'
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

class MainPost(models.Model):
    def __str__(self):
        return f'#{self.id} {self.title}'
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    body = models.CharField(verbose_name='Текст', max_length=255)
    image_url = models.CharField(verbose_name='URL-картинки', max_length=1023)

class BlogPost(models.Model):
    def __str__(self):
        return f'#{self.id} {self.title}'
    author_name = models.CharField(verbose_name='Автор поста', max_length=255, default='x')
    avatar = models.CharField(verbose_name='Аватарка автора', max_length=1023, default='x')

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    body = models.CharField(verbose_name='Текст', max_length=255)
    image_url = models.CharField(verbose_name='URL-картинки', max_length=1023)
