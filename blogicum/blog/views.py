from django.shortcuts import get_object_or_404, render
from blog.models import Category, Post
import datetime


def index(request):
    post_list = Post.objects.select_related(
        'category',
        'location'
    ).filter(is_published=True,
             category__is_published=True,
             pub_date__lte=datetime.datetime.now()
             ).order_by('-created_at')[0:5]

    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.select_related(
            'category',
            'location'
        ),
        pk=pk,
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.datetime.now())

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    post_list = Post.objects.select_related(
        'category',
        'location'
    ).filter(category__slug=category_slug,
             is_published=True,
             pub_date__lte=datetime.datetime.now())

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,)

    return render(request,
                  'blog/category.html',
                  {'post_list': post_list, 'category': category})
