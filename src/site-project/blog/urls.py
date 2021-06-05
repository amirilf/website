from django.urls import path

# import views
from .views import Home , TagView,TagsView ,ArticleView,ArticlesView,SearchView,logout_

app_name = 'blog'
urlpatterns = [
    path('',Home,name='home'),
    path('tags',TagsView,name='tags'),
    path('tags/<slug:tag_slug>',TagView,name='tag'),
    path('articles',ArticlesView,name='articles'),
    path('articles/<slug:article_slug>',ArticleView,name='article'),
    path('search',SearchView,name='search'),
    path('logout',logout_),
]
