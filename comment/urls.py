from django.urls import path
from . import views

urlpatterns = [
    path('update_comment',views.update_comment,name='update_comment'),
    path('reply_comment',views.reply_comment,name='reply_comment')
]