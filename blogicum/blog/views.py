from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

POSTS_LIMIT = 5


def get_published_post():
    return (
        Post.objects
        .select_related('author', 'location', 'category')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
    )


def index(request):
    template = 'blog/index.html'
    posts = get_published_post()[:POSTS_LIMIT]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(get_published_post(), pk=id,)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts_list = get_published_post().filter(category=category)
    context = {'post_list': posts_list, 'category': category}
    return render(request, template, context)
