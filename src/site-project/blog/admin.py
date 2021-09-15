from django.contrib import admin


# import models
from .models import Avatar, Category,Article,Comment,User

# customize models
class CategoryAdmin(admin.ModelAdmin):
	list_display  = ('name_en','name_fa','slug','status','simple_created')
	list_filter   = (['status'])
	search_fields = ('name_en','name_fa', 'slug')

class ArticleAdmin(admin.ModelAdmin):

    list_display = ('author','simple_created','slug','short_slug','title_en','views','status')
    search_fields = ('desc_en','desc_fa','title_en','title_fa','body_en','body_fa')
    ordering = ['-created']

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
            obj.save()
        return super().save_model(request, obj, form, change)   	

class CommentsAdmin(admin.ModelAdmin):

    list_display = ('name','comment_desc','created','article_slug','status')
    ordering = ['-created']



# register models
admin.site.register(User)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentsAdmin)
admin.site.register(Avatar)
