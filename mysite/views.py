from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render

from blog.models import Blog
from read_statistics.utils import seven_days_read_data


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = seven_days_read_data(blog_content_type)

    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    return render(request, 'home.html', context)


