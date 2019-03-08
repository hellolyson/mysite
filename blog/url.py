from django.urls import path

from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('int:<blog_pk>', views.blog_detail, name='blog_detail'),
    path('type/int:<blog_category_pk>', views.blog_category, name='blog_category'),
    path('date<int:year><int:month>', views.blog_with_date, name='blog_with_date')
]
