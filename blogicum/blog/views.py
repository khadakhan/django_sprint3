from django.shortcuts import get_object_or_404, render

from django.utils.timezone import now

from blog.models import Category, Post

from blog.myconst import NUM_OF_ROWS


def posts_filtered():
    return (Post.objects.select_related('category', 'location')
            .filter(is_published=True,
                    category__is_published=True,
                    pub_date__lte=now())
            )


def index(request):
    post_list = posts_filtered()[:NUM_OF_ROWS]

    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        posts_filtered(),
        pk=post_id
    )

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=now()
    )

    return render(request,
                  'blog/category.html',
                  {'post_list': post_list, 'category': category})
