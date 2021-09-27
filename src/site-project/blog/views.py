from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, redirect, render,get_object_or_404
from django.db.models import Q
# category model
from .models import Article, Category, Comment,Avatar,User

# forms
from .forms import CommentForm

# class base views dependent modules
from django.views.generic import ListView


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



#======== Tags View

# Custom :
# def TagsView(request):
#     categories_query = Category.objects.active()   # get all active categories
#     paginator        = Paginator(categories_query,10)
#     page             = request.GET.get('p')
#     categories       = paginator.get_page(page)
#     context = {
#         'categories':categories,
#         'page':'tags'
#     }
#     return render(request,'tags.html',context)

# ClassBase :
class TagsListView(ListView):
    queryset      = Category.objects.active()
    queryset      = [category for category in queryset if len(category.articles.active()) > 0]
    template_name = 'tags.html'
    context_object_name = 'categories'
    paginate_by   = 20
    page_kwarg    = 'p'

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context["page"] = 'tags'
        return context
    


#======== Tag View
# def TagView(request,tag_slug):
#     try:
#         the_query = Category.objects.filter(slug=tag_slug,articles__isnull=False)[0]
#         context = {
#             'tag':the_query
#             }
#         return render(request,'tag.html',context)
#     except:
#         raise Http404()

class TagListView(ListView):
    template_name = "tag.html"
    context_object_name = 'articles'
    paginate_by = 5
    page_kwarg  = 'p'

    def get_queryset(self):
        global category_object
        tag_slug = self.kwargs.get('tag_slug')
        category_object = get_object_or_404(Category.objects.active(),slug=tag_slug)
        return category_object.articles.active()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = category_object
        return context



#======== Article View
def ArticleView(request,article_slug):
    article_query      = get_object_or_404(Article.objects,slug=article_slug,status=True)
    comments_query     = article_query.comments.filter(reply_to=None,status=True)
    avatars_query      = Avatar.objects.all()
    
    # add 1 view to article
    Article.objects.active().filter(slug=article_slug).update(views=article_query.views+1)
    
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
                new_comment_form.admin  = User.objects.get(username=request.user.username)
                new_comment_form.status = True 
            
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




#======== Articles View

# Custom :
# def ArticlesView(request):
#     articles_query = get_list_or_404(Article.objects.active())
#     paginator      = Paginator(articles_query,5)
#     page           = request.GET.get('p')
#     articles       = paginator.get_page(page)
#     context        = {
#         'articles':articles,
#     }
#     return render(request,'articles.html',context)

# ClassBase :
class ArticlesListView(ListView):
    queryset      = get_list_or_404(Article.objects.active())
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by   = 5
    page_kwarg = 'p'



#======== Search View
def SearchView(request):
    try:
        search_query = str(request.GET['q']).strip()
        if len(search_query) < 2 or search_query.isspace():
            error = True
            search_query = ''
            article_results = []
            category_results = []
        else:
            error = False
            article_results = Article.objects.active().filter( Q(title_en__icontains = search_query) | Q(desc_en__icontains = search_query) )
            category_results = Category.objects.active().filter(name_en__icontains=search_query)
            category_results = [item for item in category_results if len(item.articles.active()) > 0] 
    except:
        error = False
        search_query = ''
        article_results = []
        category_results = []
    context = {
        'search':search_query,
        'page':'search',
        'articles':article_results,
        'categories':category_results,
        'error' : error           
    }
    return render(request,'search.html',context)

# class SearchListView(ListView):
#     template_name = 'search.html'

#     def get_queryset(self):
#         if self.kwargs.get('q'):
#             search_query = self.kwargs.get('q')
#             article_results = Article.objects.active().filter( Q(title_en__icontains = search_query) | Q(desc_en__icontains = search_query) )
#             category_results = Category.objects.active_search().filter(name_en__icontains=search_query)
#             category_results = [item for item in category_results if len(item.articles.active()) > 0] 
#         else:
#             search_query = ''
#             article_results = []
#             category_results = []
        


#======== ShortSlug View
def ShortSlugView(request,short_slug_url):
    article_query = get_object_or_404(Article.objects,status=True,short_slug=short_slug_url)
    article_url   = article_query.slug
    return redirect(f'/articles/{article_url}')



#======== Authors View
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



#======== CommentsValidation View
def comments_check(request):
    if request.user.is_authenticated:
        unspecified_comments = Comment.objects.filter(status=False)
        context = {
            'comments' : unspecified_comments
        }
        return render(request,'comments.html',context=context)
    else:
        raise Http404()

def comment_delete(request,pk_id):
    if request.user.is_authenticated:
        try:
            comment = Comment.objects.get(pk=pk_id)
            comment.delete()
            return HttpResponse('deleted')
        except:
            raise Http404()
    else:
        raise Http404()

def comment_confirm(request,pk_id):
    if request.user.is_authenticated:
        try:
            comment = Comment.objects.filter(pk=pk_id)
            if comment[0].status == False:
                comment.update(status=True)
                return HttpResponse('confirmed')
            else:
                raise Http404()
        except:
            raise Http404()
    else:
        raise Http404()



#======== SendEmail View
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# def send_email_(request):
#     msg_plain = render_to_string('email.txt', {'username': 'Amir Khorasani'})
#     msg_html = render_to_string('email.html', {'username': 'Amir Khorasani'})
    
#     send_mail(
#         'Hi there',
#         msg_plain,
#         'amirctw@gmail.com',
#         ['amirilf@protonmail.com'],
#         html_message=msg_html,
#     )
#     return HttpResponse('message sented (:')
