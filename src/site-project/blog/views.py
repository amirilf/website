from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_list_or_404, redirect, render,HttpResponse,get_object_or_404
from django.db.models import Q

# category model
from .models import Article, Category, Comment,Avatar,User

# forms
from .forms import CommentForm

# views


#======== home
def Home(request):
    articles_query     = Article.objects.active()     # get all active articles
    articles_latest    = articles_query.order_by('-created')[:3]  # get 3 latest articles
    articles_mostvisit = articles_query.order_by('-views')[:3]    # get 3 most visited articles
    context = {
        'latest_articles':articles_latest,
        'most_viewed_articles':articles_mostvisit,
    }
    return render(request,'home.html',context)


#======== tags
def TagsView(request):
    categories_query   = Category.objects.active()   # get all active categories
    categories_query   = [category for category in categories_query if len(category.articles.active()) > 0] #check if length is bigger than 0 and tag already used before
    context = {
        'categories':categories_query,
        'page':'tags'
    }
    return render(request,'tags.html',context)

def TagView(request,tag_slug):
    try:
        the_query = Category.objects.filter(slug=tag_slug,articles__isnull=False)[0]
        context = {
            'tag':the_query
            }
        return render(request,'tag.html',context)
    except:
        raise Http404()


#======== articles
def ArticleView(request,article_slug):
    article_query      = get_object_or_404(Article.objects,slug=article_slug,status=True)
    comments_query     = article_query.comments.filter(status=True,reply_to=None)
    avatars_query      = Avatar.objects.all()
    
    # add 1 view to article
    Article.objects.filter(slug=article_slug,status=True).update(views=article_query.views+1)
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            
            new_comment_form = comment_form.save(commit=False)
            new_comment_form.article = article_query

            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            
            if parent_id:
                # get parent comment
                parent_comment = Comment.objects.get(id=parent_id)
                # check if exist
                if parent_comment: 
                    # set parent comment
                    new_comment_form.reply_to = parent_comment 
            try:
                avatar_id = int(request.POST.get('articel_input'))
            except:
                avatar_id = None
            
            if avatar_id:
                # get avatar object
                avatar_obj = Avatar.objects.get(id=avatar_id)
                # check if exist
                if avatar_obj: 
                    # set avatar for comment
                    new_comment_form.avatar = avatar_obj

            if request.user.is_authenticated: # if user was admin
                new_comment_form.admin = User.objects.get(username=request.user.username)
            
            new_comment_form.save()
            return HttpResponseRedirect(article_query.get_absolute_url())

    else:
        comment_form = CommentForm()

    context = {
        'article':article_query,
        'comments':comments_query,
        'comment_form':comment_form,
        'avatars': avatars_query,
    }
    return render(request,'article.html',context)

def ArticlesView(request):
    articles_query = get_list_or_404(Article.objects.active())
    context = {
        'articles':articles_query,
    }
    return render(request,'articles.html',context)


#======== search
def SearchView(request):
    try:
        search_query = request.GET['q']
        article_results = Article.objects.active().filter( Q(title_en__icontains = search_query) | Q(desc_en__icontains = search_query) )
        category_results = Category.objects.active().filter(name_en__icontains=search_query)
    except:
        search_query = ''
        article_results = []
        category_results = []
    context = {
        'search':search_query,
        'page':'search',
        'articles':article_results,
        'categories':category_results,               
    }
    return render(request,'search.html',context)


#======== short slugs
def ShortSlugView(request,short_slug_url):
    article_query = get_object_or_404(Article.objects,status=True,short_slug=short_slug_url)
    article_url   = article_query.slug
    return redirect(f'/articles/{article_url}')

#======== authors
def AlirezaView(request):
    context = {
        'data' : User.objects.get(username='alireza')
    }
    return render(request,'creator.html',context=context)

def AmirView(request):
    context = {
        'data' : User.objects.get(username='amir')
    }
    return render(request,'creator.html',context=context)
