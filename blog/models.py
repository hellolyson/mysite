from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from read_statistics.models import ReadNumExpandMethod

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=20,verbose_name='博客分类')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = '博客分类'

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=50,verbose_name='标题')
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,verbose_name='博客分类')
    content = RichTextUploadingField(verbose_name='内容')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    last_update_time = models.DateTimeField(auto_now=True,verbose_name='最后一次更新时间')

    def get_url(self):
        return reverse('blog_detail',kwargs={'blog_pk':self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return '<Blog:%s>' % self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = '博客'
