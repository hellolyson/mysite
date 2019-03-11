from django.contrib import admin
from .models import ReadNum, ReadDetail


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')
    list_per_page = 30


@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')
    list_per_page = 30
    list_filter = ('date',)
    date_hierarchy = 'date'
    list_display_links = ('date','content_object')
