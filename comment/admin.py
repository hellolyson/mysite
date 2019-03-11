from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content_object','text','comment_time','user','root','parent')
    list_per_page = 50
    list_filter = ('comment_time',)
    date_hierarchy = 'comment_time'
    list_display_links = ('id','content_object','text')
