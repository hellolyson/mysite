from django.contrib import admin
from .models import BlogCategory,Blog

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']
    list_display_links = ('id','category_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','get_read_num','author','create_time','last_update_time']
    list_per_page = 20
    search_fields = ('title',)
    list_filter = ('category','create_time',)
    date_hierarchy = 'create_time'
    list_display_links = ('id','title')


admin.site.site_header = '个人博客后台管理'
admin.site.site_title = '个人博客后台管理'

