from django.urls import path

# import views
from .views import AlirezaView, AmirView, Home, ShortSlugView , TagView,TagsView ,ArticleView,ArticlesView,SearchView, comment_confirm, comment_delete, comments_check, send_email_

app_name = 'blog'
urlpatterns = [
    path('',Home,name='home'),
    path('tags',TagsView,name='tags'),
    path('tags/<slug:tag_slug>',TagView,name='tag'),
    path('articles',ArticlesView,name='articles'),
    path('articles/<slug:article_slug>',ArticleView,name='article_slug'),
    path('search',SearchView,name='search'),
    path('amir',AmirView),
    path('alireza',AlirezaView),
    path('comments',comments_check),
    path('comments/delete/<int:pk_id>',comment_delete,name='delete_comment'),
    path('comments/confirm/<int:pk_id>',comment_confirm,name='confirm_comment'),
    path('email',send_email_),
    # the last one for shortcuts
    path('<slug:short_slug_url>',ShortSlugView),
]

