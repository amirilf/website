from django.http.response import Http404
from django.shortcuts import get_list_or_404, render,HttpResponse,get_object_or_404


# website dynamic data
from . import contents


# category model
from .models import Article, Category


# views


def Home(request):
    categories_query   = Category.objects.active()    # get all active categories
    articles_query     = Article.objects.active()     # get all active articles
    articles_latest    = articles_query.order_by('-created')[:3]  # get 3 latest articles
    articles_mostvisit = articles_query.order_by('-views')[:3]    # get 3 most visited articles
    context = {
        'categories':categories_query,
        'latest_articles':articles_latest,
        'most_viewed_articles':articles_mostvisit,
        'site_setting':contents,
    }
    return render(request,'home.html',context)



def TagsView(request):
    categories_query   = Category.objects.active()    # get all active categories
    context = {
        'categories':categories_query,
    }
    return render(request,'tags.html',context)



def TagView(request,tag_slug):
    try:
        the_query = Category.objects.get(slug=tag_slug,status=True)
        return HttpResponse(f'tag : {the_query.name_en} {the_query.name_fa}')
    except:
        raise Http404()


def ArticleView(request,article_slug):
    categories_query   = Category.objects.active()    # get all active categories
    article_query = get_object_or_404(Article.objects,slug=article_slug,status=True)
    Article.objects.filter(slug=article_slug,status=True).update(views=article_query.views+1)
    context = {
        'categories':categories_query,
        'article':article_query,
        'site_setting':contents,
    }
    return render(request,'article.html',context)


def ArticlesView(request):
    categories_query   = Category.objects.active()    # get all active categories
    articles_query = get_list_or_404(Article.objects,status=True)
    context = {
        'categories':categories_query,
        'articles':articles_query,
        'site_setting':contents,
    }
    return render(request,'articles.html',context)


def SearchView(request):
    return render(request,'search.html')


from django.contrib.auth import logout
def logout_(request):
    logout(request)
    return HttpResponse(f'Hi {request.user}')