from django.urls import path,re_path

# import views
from .views import (
    Home,
    TagsListView,
    TagListView,
    ArticlesListView,
    ArticleView,
    AmirView,
    AlirezaView,
    AuthorArticlesView,
    SearchView,
    Comment_confirm,
    Comment_delete,
    Comments_check,
    ShortSlugView,
)

app_name = 'blog'
urlpatterns = [
    path('',Home,name='home'),

    # tags section
    path('tags',TagsListView.as_view(),name='tags'),
    path('tags/<slug:tag_slug>',TagListView.as_view(),name='tag'),
    
    # articles section
    path('articles',ArticlesListView.as_view(),name='articles'),
    path('articles/<slug:article_slug>',ArticleView,name='article_slug'),
    
    # search section
    path('search',SearchView,name='search'),
    
    # authors section
    path('amir',AmirView),
    path('alireza',AlirezaView),
    re_path('(?P<author>(amir|alireza))/articles',AuthorArticlesView.as_view(),name='author-articles'),
    
    # check comments section
    path('comments',Comments_check),
    path('comments/delete/<int:pk_id>',Comment_delete,name='delete_comment'),
    path('comments/confirm/<int:pk_id>',Comment_confirm,name='confirm_comment'),
    
    # the last one for shortcuts
    path('<slug:short_slug_url>',ShortSlugView),
]

