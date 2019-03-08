from django.contrib import admin
from .models import BlogCategory,Blog

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','get_read_num','author','create_time','last_update_time']




