from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from blog.models import Category, Post
from blog.const import NUMBER_OF_POSTS_ON_MAIN_PAGE


def posts_filtered_by_published(manager_of_posts):
    return manager_of_posts.select_related(
        'category',
        'location',
        'author').filter(is_published=True,
                         category__is_published=True,
                         pub_date__lte=now())


def index(request):
    post_list = posts_filtered_by_published(
        Post.objects
    )[:NUMBER_OF_POSTS_ON_MAIN_PAGE]

    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        posts_filtered_by_published(Post.objects),
        pk=post_id
    )

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = posts_filtered_by_published(
        category.posts.all()
    )

    return render(request,
                  'blog/category.html',
                  {'post_list': post_list, 'category': category})
