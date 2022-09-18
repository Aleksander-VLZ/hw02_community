from django.db import models
# Из модуля auth импортируем функцию get_user_model
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):  # наследник класса Model из модуля models
    title = models.CharField(max_length=200)  # название сообщества
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField()  # описание сообщества

    def __str__(self) -> str:
        return self.title


class Post(models.Model):  # наследник класса Model из модуля models
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="posts"
    )
