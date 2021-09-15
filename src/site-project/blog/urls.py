from django.urls import path

# import views
from .views import AlirezaView, AmirView, Home, ShortSlugView , TagView,TagsView ,ArticleView,ArticlesView,SearchView, comment_confirm, comment_delete, comments_check

app_name = 'blog'
urlpatterns = [
    path('',Home,name='home'),
    path('tags',TagsView,name='tags'),
    path('tags/p/<int:page_id>',TagsView,name='tag_page'),
    path('tags/<slug:tag_slug>',TagView,name='tag'),
    path('articles',ArticlesView,name='articles'),
    path('articles/p/<int:page_id>',ArticlesView,name='article_page'),
    path('articles/<slug:article_slug>',ArticleView,name='article'),
    path('search',SearchView,name='search'),
    path('amir',AmirView),
    path('alireza',AlirezaView),
    path('comments',comments_check),
    path('comments/delete/<int:pk_id>',comment_delete,name='delete_comment'),
    path('comments/confirm/<int:pk_id>',comment_confirm,name='confirm_comment'),

    # the last one for shortcuts
    path('<slug:short_slug_url>',ShortSlugView),
]

