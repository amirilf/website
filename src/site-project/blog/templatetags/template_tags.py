from django import template

register = template.Library()


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
