from django.shortcuts import get_object_or_404, render
from blog.models import Category, Post
import datetime


def index(request):
    post_list = Post.objects.values(
        'id',
        'title',
        'text',
        'pub_date',
        'location',
        'location__name',
        'location__is_published',
        'author__username',
        'category__title',
        'category__slug'
    ).filter(is_published=True,
             category__is_published=True,
             pub_date__lte=datetime.datetime.now()
             ).order_by('-created_at')[0:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.values(
            'id',
            'title',
            'text',
            'pub_date',
            'location',
            'location__name',
            'location__is_published',
            'author__username',
            'category__title',
            'category__slug',
            'category__description'
        ).filter(is_published=True,
                 pk=pk,
                 category__is_published=True,
                 pub_date__lte=datetime.datetime.now()),
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
        category__is_published=True)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    post_list_body = Post.objects.values(
        'id',
        'title',
        'text',
        'pub_date',
        'location',
        'location__name',
        'location__is_published',
        'author__username',
        'category__title',
        'category__slug',
        'category__description'
    ).filter(category__slug=category_slug,
             is_published=True,
             category__is_published=True,
             pub_date__lte=datetime.datetime.now())

    post_list_head = get_object_or_404(
        Category.objects.values(
            'title',
            'description',
            'slug'
        ).filter(slug=category_slug),
        slug=category_slug)

    return render(request,
                  'blog/category.html',
                  {'post_list_body': post_list_body,
                   'post_list_head': post_list_head})
