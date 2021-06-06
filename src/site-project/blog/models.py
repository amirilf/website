from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateTimeField, SlugField

# user model , django default
from django.contrib.auth.models import AbstractUser

# ckeditor field
from ckeditor_uploader.fields import RichTextUploadingField



# random str
from django.utils.crypto import get_random_string
letters_random = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# auto created slug func
def auto_slug(obj,checker):
    if checker == 0:
        # for article
        if not obj.short_slug :
            obj.short_slug = get_random_string(3,letters_random)
            while True:
                exists_list = type(obj).objects.filter(short_slug=obj.short_slug)
                if not exists_list:
                    break
                obj.short_slug = get_random_string(3,letters_random)
    else:
        # for category
        if not obj.slug :
            obj.slug = get_random_string(3,letters_random)
            while True:
                exists_list = type(obj).objects.filter(slug=obj.slug)
                if not exists_list:
                    break
                obj.slug = get_random_string(3,letters_random)






# Managers

class CategoryManager(models.Manager):
	def active(self):
		return self.filter(status=True)

class ArticleManager(models.Manager):
	def active(self):
		return self.filter(status=True)







# models

class User(AbstractUser):
    thumbnail  = models.ImageField(upload_to='creators',default='creators/default.png')



class Category(models.Model):
    name_en = CharField(max_length=100) # English name
    name_fa = CharField(max_length=100) # Persian name
    slug    = SlugField(editable=False) #auto created in auto_slug_category function
    created = DateTimeField(auto_now_add=True) # auto complete created time
    status  = BooleanField(default=True) # category status => true:publish , false:draft

    class Meta:
        verbose_name_plural = 'Categories'
        ordering            = ['-created'] # for new to old sorting in admin panel 

    def __str__(self):
        return self.name_en

    objects = CategoryManager() # set managers for this class

    # return yyyy/mm/dd hh:mm format of created field
    def simple_created(self):
        return self.created.strftime("%Y/%m/%d %H:%M")
    simple_created.short_description = "created"


    def save(self, *args, **kwargs):
        auto_slug(self,1)
        super(Category, self).save(*args, **kwargs)



class Article(models.Model):
    title_en   = models.CharField(max_length=200) # english title
    title_fa   = models.CharField(max_length=200) # persian title
    desc_en    = models.TextField() # english description for article in home
    desc_fa    = models.TextField() # persian description for article in home
    body_en    = RichTextUploadingField() # english body
    body_fa    = RichTextUploadingField() # persian body
    slug       = models.SlugField(max_length=100,unique=True) # slug of the article
    short_slug = models.SlugField(editable=False) # auto created in auto_slug_article function
    views      = models.IntegerField(default=0) # number of views this article
    status     = models.BooleanField(default=True) # article status => true:publish , false:draft
    created    = models.DateTimeField(auto_now_add=True) # auto complete created time
    updated    = models.DateTimeField(auto_now=True) # auto compelete last update
    author     = models.ForeignKey(User,editable=False,null=True,on_delete=models.SET_NULL) # auto delete article on delete author
    category   = models.ManyToManyField(Category,blank=True,related_name='articles') # article categories
    thumbnail  = models.ImageField(upload_to='thumbnails') # article thumbnail in post card and main page
    readtime   = models.IntegerField(default=0) # suggested time for readnig the article

    class Meta:
        verbose_name_plural = 'Articles'
        ordering            = ['-created'] # for new to old sorting in admin panel 

    def __str__(self):
        return self.title_en

    def get_absolute_url(self):
        return f'/articles/{self.slug}'
    

    objects = ArticleManager() # set managers for this class

    # return yyyy/mm/dd hh:mm format of created field
    def simple_created(self):
        return self.created.strftime("%Y/%m/%d %H:%M")
    simple_created.short_description = "created"

    # changes when article fields saves
    def save(self, *args, **kwargs):
        auto_slug(self,0)
        super(Article, self).save(*args, **kwargs)


class Comment(models.Model):
    # author    = models.ForeignKey(User,editable=False,null=True,on_delete=models.SET_NULL) # auto delete article on delete author
    article  = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    name     = CharField(max_length=50)
    desc     = RichTextField()
    created  = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='replies')
    status   = models.BooleanField(default=True) # comment status => true:publish , false:draft
    
  
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        if self.reply_to:
            return f'Comment by {self.name} reply to {self.reply_to}'
        else:
            return f'Comment by {self.name}'
