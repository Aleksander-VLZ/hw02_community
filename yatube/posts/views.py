# yatube/views.py
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group

LAST_POSTS: int = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:LAST_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# Для страницы, на которой будут посты, отфильтрованные по группам;
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект,
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе.
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:LAST_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
