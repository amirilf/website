from django.template import Library
from ..models import Category,User
from .. import contents

register = Library()


# it's for using dynamic data (content.py) in templates
@register.simple_tag
def site_setting(value):
    try:
        return contents.data_set[value]
    except:
        pass


@register.simple_tag
def calculate_latest_5_page_numbers(last_page_number):
    return last_page_number - 5


@register.inclusion_tag('partials/col_4_about.html')
def col_4_about():
    return {
        'col_4_about': contents.data_set['about']
    }


@register.inclusion_tag('partials/col_4_tags.html')
def col_4_tags():
    categories_query          = Category.objects.active()   # get all active categories
    categories_query          = [category for category in categories_query if len(category.articles.active()) > 0] #check if length is bigger than 0 and tag already used before
    if len(categories_query) <= contents.data_set['col_4_tags_count']:
        return {
            'fix' : True,
            'col_4_tags': categories_query,
        }
    else:
        return {
            'fix' : False,
            'col_4_tags': categories_query[:contents.data_set['col_4_tags_count']],
        }


@register.inclusion_tag('partials/col_4_social.html')
def col_4_social():
    creators = User.objects.filter(is_superuser=True)
    return {
            'creators': creators,
        }
