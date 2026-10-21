from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    posts = (
        Post.objects
        .select_related('author', 'location', 'category')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
        .order_by('-pub_date')[:5]
    )
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects
        .select_related('author', 'location', 'category')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        ),
        pk=id,
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = (
        Post.objects
        .select_related('author', 'location', 'category')
        .filter(
            category=category,
            pub_date__lte=timezone.now(),
            is_published=True,
        )
        .order_by('-pub_date')
    )
    context = {'post_list': posts, 'category': category}
    return render(request, template, context)