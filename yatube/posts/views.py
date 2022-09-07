# yatube/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Для страницы, на которой будут посты, отфильтрованные по группам;
# view-функция принимает параметр pk из path()
def group_posts(request, pk):
    return HttpResponse(f'Пост {pk}')