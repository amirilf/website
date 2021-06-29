from django.template import Library
from ..models import Category,User
from ..contents import about,col_4_tags_count


register = Library()

@register.simple_tag
def author_full_name(author):
    if author.first_name:
        return f'{author.first_name.capitalize()} {author.last_name.capitalize()}'
    else:
        return author.username.capitalize()
    
@register.simple_tag
def author_first_name(author):
    if author.first_name:
        return author.first_name.capitalize()
    else:
        return author.username.capitalize()


@register.inclusion_tag('partials/col_4_about.html')
def col_4_about():
    return {
        'col_4_about': about
    }


@register.inclusion_tag('partials/col_4_tags.html')
def col_4_tags():
    categories_query   = Category.objects.active()   # get all active categories
    categories_query   = [category for category in categories_query if len(category.articles.active()) > 0] #check if length is bigger than 0 and tag already used before
    if len(categories_query) <= col_4_tags_count:
        return {
            'fix' : True,
            'col_4_tags': categories_query,
        }
    else:
        return {
            'fix' : False,
            'col_4_tags': categories_query[:col_4_tags_count],
        }

@register.inclusion_tag('partials/col_4_social.html')
def col_4_social():
    creators = User.objects.filter(is_superuser=True)
    return {
            'creators': creators,
        }
