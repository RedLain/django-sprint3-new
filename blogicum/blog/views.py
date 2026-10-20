from django.http import Http404
from django.shortcuts import render


def index(request):
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    for detail_post in posts:
        if detail_post['id'] == id:
            context = {'post': detail_post}
            return render(request, 'blog/detail.html', context)
    raise Http404('Пост не найден')


def category_posts(request, category_slug):
    context = {'category_slug': category_slug}
    return render(request, 'blog/category.html', context)
