# Generated by Django 2.0 on 2019-03-11 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20190307_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='comment.Comment', verbose_name='父节点'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL, verbose_name='回复谁'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_comment', to='comment.Comment', verbose_name='根节点'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
    ]
