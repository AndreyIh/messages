from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.TextField(verbose_name='Сообщение')
    media_file = models.ImageField(upload_to='image/%Y/%m/%d', blank=True, verbose_name='Прикрепленное изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор сообщения')
    create_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.author} ({self.create_time}): {self.content} {self.media_file}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['create_time']
