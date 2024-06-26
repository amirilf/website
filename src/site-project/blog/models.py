# =============== Imports

from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField, SlugField
from ckeditor.fields import RichTextField
from django.urls import reverse

# user model , django default
from django.contrib.auth.models import AbstractUser

# ckeditor field
from ckeditor_uploader.fields import RichTextUploadingField

# dynamic data in website
from .contents import data_set



# =============== Auto Slug

# random str
from django.utils.crypto import get_random_string
letters_random = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# auto created slug func
def auto_slug(obj,checker):
    if checker == 0:
        # slug for article
        if not obj.short_slug : # article may be in editing mode
            obj.short_slug = get_random_string(3,letters_random)
            while True:
                exists_list = type(obj).objects.filter(short_slug=obj.short_slug) # set slug in model
                if not exists_list:
                    break
                obj.short_slug = get_random_string(3,letters_random)
    else:
        # slug for category
        if not obj.slug : # category may be in editing mode
            obj.slug = get_random_string(3,letters_random)
            while True:
                exists_list = type(obj).objects.filter(slug=obj.slug) # set slug in model
                if not exists_list:
                    break
                obj.slug = get_random_string(3,letters_random)



# =============== Managers

class ArticleManager(models.Manager):
	def active(self):
		return self.filter(status=True)

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
        
class CommentsManager(models.Manager):
    def active(self):
        return self.filter(status=True)



# =============== Models

# customize user model
class User(AbstractUser):
    thumbnail     = models.ImageField(upload_to='creators',default='creators/default.png')
    telegram      = models.URLField(null=True,blank=True)
    instagram     = models.URLField(null=True,blank=True)
    linkedin     = models.URLField(null=True,blank=True)
    github        = models.URLField(null=True,blank=True)
    user_page_url = models.CharField(max_length=200)
    desc          = RichTextField(null=True)
    skills        = models.CharField(max_length=500,null=True,help_text='pls separate the skills by 3')
    
    # to identify skills
    def get_skills(self):
        skills_list = self.skills.split('-')
        return skills_list

    # capital version of get_full_name
    def full_capital_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
        else:
            return self.username.capitalize()

    # return short name for article inform line
    def get_first_name(self):
            if self.first_name:
                return self.first_name.capitalize()
            else:
                return self.username.capitalize()

    # get user page url with / at first
    def get_user_page_url(self):
        return f'/{self.user_page_url}'

class Category(models.Model):
    name_en    = CharField(max_length=100) # English name
    slug       = SlugField(editable=False) # auto created in auto_slug_category function
    created    = DateTimeField(auto_now_add=True) # auto complete created time
    status     = BooleanField(default=True) # category status => true:publish , false:draft
    thumbnail  = models.ImageField(upload_to='categories',null=True) # article thumbnail in post card and main page

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
    desc_en    = models.TextField() # english description for article in home
    body_en    = RichTextUploadingField() # english body
    slug       = models.SlugField(max_length=100,unique=True) # slug of the article
    short_slug = models.SlugField(editable=False) # auto created in auto_slug_article function
    views      = models.IntegerField(default=0) # number of views this article
    status     = models.BooleanField(default=True) # article status => true:publish , false:draft
    created    = models.DateTimeField(auto_now_add=True) # auto complete created time
    updated    = models.DateTimeField(auto_now=True) # auto compelete last update
    author     = models.ForeignKey(User,editable=False,null=True,on_delete=models.SET_NULL,related_name='articles') # auto delete article on delete author
    category   = models.ManyToManyField(Category,blank=True,related_name='articles') # article categories
    thumbnail  = models.ImageField(upload_to='articles') # article thumbnail in post card and main page
    readtime   = models.IntegerField(default=0) # suggested time for readnig the article

    class Meta:
        verbose_name_plural = 'Articles'
        ordering            = ['-created'] # for new to old sorting in admin panel 

    def __str__(self):
        return self.title_en

    def get_absolute_url(self):
        return reverse("blog:article_slug",kwargs={'article_slug':self.slug})
        # return f'/articles/{self.slug}' these are same but top is better

    objects = ArticleManager() # set managers for this class

    # return yyyy/mm/dd hh:mm format of created field
    def simple_created(self):
        return self.created.strftime("%Y/%m/%d")
    simple_created.short_description = "created"

    # changes when article fields saves
    def save(self, *args, **kwargs):
        auto_slug(self,0)
        super(Article, self).save(*args, **kwargs)


class Avatar(models.Model):
    thumbnail = models.ImageField(upload_to='avatars') # avatars images for comments


class Comment(models.Model):
    admin    = models.ForeignKey(User,editable=False,default=None,null=True,on_delete=models.SET_NULL)
    article  = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    name     = CharField(max_length=50)
    desc     = RichTextField()
    created  = models.DateTimeField(auto_now_add=True) # date of comment creation
    reply_to = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='replies') # for reply comments
    status   = models.BooleanField(default=False) # comment status => true:publish , false:draft
    avatar   = models.ForeignKey(Avatar,on_delete=models.SET_NULL,null=True) # comment avatar => has default and auto customize for admins
  
    class Meta:
        ordering = ('-created',)
    
    # show comment information in panel
    def __str__(self):
        if self.reply_to:
            return f'Comment by {self.name} reply to {self.reply_to}'
        else:
            return f'Comment by {self.name}'

    objects = CommentsManager() # set managers for this class
    
    # short-show comments in admin panel
    def comment_desc(self):
        if len(self.desc) > 53:
            return f'{self.desc[:50]}...'
        else:
            return self.desc
