from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from blog.models import Blog
from blog.views import get_blog_list_common_data
from read_statistics.utils import seven_days_read_data


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    new_blog_list = Blog.objects.all()[:7]
    dates, read_nums = seven_days_read_data(blog_content_type)

    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    context['new_blog_list'] = new_blog_list
    return render(request, 'home.html', context)

def search(request):
    keyWord = request.GET.get('keyword',None)
    if keyWord:
        blogs_all_list = Blog.objects.filter(title__contains=keyWord)
        context = get_blog_list_common_data(request, blogs_all_list)
        context['keyWord'] = keyWord
        return render(request,'search_keyword.html',context)


