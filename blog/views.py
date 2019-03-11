from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count

from mysite.settings.development import EACH_PAGE_BLOGS_NUMBER
from .models import Blog, BlogCategory
from read_statistics.utils import read_statistics_once_read


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_range'] = page_range
    context['page_of_blogs'] = page_of_blogs
    context['blogcategory'] = BlogCategory.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = Blog.objects.dates('create_time', 'month', order='DESC')
    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render(request, 'blog/blog_list.html', context)


def blog_category(request, blog_category_pk):
    blog_category = get_object_or_404(BlogCategory, pk=blog_category_pk)
    blogs_all_list = Blog.objects.filter(category=blog_category)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['category'] = blog_category
    return render(request, 'blog/category.html', context)


def blog_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(create_time__year=year, create_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)
    return render(request, 'blog/blogs_with_date.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request, blog)

    context = {}
    context['previous_blog'] = Blog.objects.filter(create_time__gt=blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(create_time__lt=blog.create_time).first()
    context['blog'] = blog
    response = render(request, 'blog/blog_detail.html', context)
    response.set_cookie(read_cookie_key, 'true')
    return response
